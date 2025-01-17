import serial
import csv
import time
import signal
import sys

# Global flag to handle termination
running = True

def signal_handler(sig, frame):
    """
    Handles termination signal (Ctrl+C) to stop the script gracefully.
    """
    global running
    print("\nStopping data collection...")
    running = False

def send_at_command(serial_port, command, timeout=0.005):
    """
    Sends an AT command to the modem and reads the response.

    Args:
        serial_port (serial.Serial): The serial port object.
        command (str): The AT command to send.
        timeout (int): Timeout in seconds for the response.

    Returns:
        str: The raw response from the modem.
    """
    serial_port.write((command + '\r').encode())
    time.sleep(timeout)
    response = serial_port.read_all().decode().strip()
    return response

def parse_qeng_servingcell(response):
    """
    Parses the AT+QENG="servingcell" response for NR5G-SA fields.

    Args:
        response (str): The raw response string from the modem.

    Returns:
        dict: A dictionary containing extracted fields.
    """
    try:
        if "+QENG: " in response:
            response = response.split("+QENG: ")[1]
        fields = response.strip().split(',')

        # Map the fields based on the documented response format
        result = {
            "state": fields[1].strip('"'),             # Connection state
            "mode": fields[2].strip('"'),              # Network mode
            "duplex_mode": fields[3].strip('"'),       # Duplex mode
            "mcc": int(fields[4]),                    # Mobile Country Code
            "mnc": int(fields[5]),                    # Mobile Network Code
            "cell_id": int(fields[6]),                # Cell ID
            "pcid": int(fields[7]),                   # Physical Cell ID
            "tac": int(fields[8]),                    # Tracking Area Code
            "arfcn": int(fields[9]),                  # Absolute Radio Frequency Channel Number
            "band": fields[10].strip('"'),            # Band info
            "nr_dl_bandwidth": int(fields[11]),       # Downlink bandwidth
            "rsrp": int(fields[12]),                  # Reference Signal Received Power
            "rsrq": int(fields[13]),                  # Reference Signal Received Quality
            "sinr": int(fields[14]),                  # Signal-to-Interference plus Noise Ratio
            "tx_power": int(fields[15]),              # Transmit power
            #"srxlev": int(fields[16])                 # Signal reception level
        }

        return result

    except (IndexError, ValueError) as e:
        raise ValueError("Invalid response format. Check input.") from e

def parse_qnwcfg_nr5g_csi(response):
    """
    Parses the AT+QNWCFG="nr5g_csi" response and extracts CQI.

    Args:
        response (str): The raw response string from the modem.

    Returns:
        int: The extracted CQI value.
    """
    try:
        if "AT+" in response:
            response = response.split("\n")[1]
        if "+QNWCFG:" in response:
            # Extract the relevant part of the response after the +QNWCFG marker
            response = response.split("+QNWCFG: \"nr5g_csi\",")[1]
            # Split by commas to get the values
            values = response.split(',')
            # Extract CQI (assuming it's the third value in the list)
            cqi = int(values[2].strip())
            return cqi
        else:
            raise ValueError("Invalid response format.")
    except (IndexError, ValueError) as e:
        raise ValueError("Failed to parse CQI from the response.") from e

def save_to_csv(filename, data, headers):
    """
    Saves data to a CSV file.

    Args:
        filename (str): The name of the CSV file.
        data (list): A list of dictionaries containing the data.
        headers (list): The column headers for the CSV.
    """
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        # Write headers only if the file is empty
        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(data)

def main():
    global running

    # Configure the serial port
    serial_port = serial.Serial(
        port='/dev/ttyUSB3',  # Update with the correct port for your modem
        baudrate=115200,
        timeout=1
    )

    # CSV file setup
    output_file = "metrics_with_timestamps.csv"
    headers = [
        "timestamp", "state", "mode", "duplex_mode", "mcc", "mnc", "cell_id", "pcid",
        "tac", "arfcn", "band", "nr_dl_bandwidth", "rsrp", "rsrq", "sinr",
        "tx_power", "srxlev", "cqi"
    ]

    print("Collecting data... Press Ctrl+C to stop.")
    try:
        while running:
            # Collect a single sample for serving cell data
            response = send_at_command(serial_port, 'AT+QENG="servingcell"')
            print("Serving Cell Data:", response)
            if "AT+" in response:
                response = response.split("\n")[1]
            if "+QENG:" in response:
                parsed_data = parse_qeng_servingcell(response)
                # Collect CQI data
                cqi_response = send_at_command(serial_port, 'AT+QNWCFG="nr5g_csi"')
                print("CQI Data:", cqi_response)
                
                cqi = parse_qnwcfg_nr5g_csi(cqi_response)

                # Add CQI to the parsed data
                parsed_data["cqi"] = cqi

                # Add current timestamp to the data
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                parsed_data["timestamp"] = timestamp

                print(parsed_data)  # Print the data for monitoring
                save_to_csv(output_file, [parsed_data], headers)
                
                time.sleep(0.1)  # Wait 1 second before the next sample         
            else:
                print("No valid response for serving cell. Retrying...")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        serial_port.close()
        print("Serial port closed. Exiting program.")

if __name__ == "__main__":
    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    main()
