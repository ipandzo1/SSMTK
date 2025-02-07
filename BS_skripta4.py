import json
import csv
from websocket import create_connection
import time

def main():
    # Server address
    server = "100.100.129.30:9001"
    
    # API call message
    message = "{\"message\": \"ue_get\", \"stats\": true}"

    # Establish WebSocket connection
    ws = create_connection("ws://" + server)
    print("Connected to server: ws://" + server)

    # Send the API call message
    ws.send(message)
    print("Message sent:", message)

    # Prepare the CSV file for writing
    csv_file = "output_with_current_timestamps_3.csv"
    with open(csv_file, mode="a", newline="", encoding="utf-8") as file:  # Use 'a' to append data
        csv_writer = csv.writer(file)

        # Keep track of written headers
        header_written = False

        while True:
            # Receive and parse the result
            result = ws.recv()
            if result:
                parsed_message = json.loads(result)
                print("Full parsed message:")
                print(json.dumps(parsed_message, indent=2, ensure_ascii=False))

                # Get the current timestamp
                current_timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                # Extract `ue_list`
                ue_list = parsed_message.get("ue_list", [])
                
                for ue in ue_list:
                    ran_ue_id = ue.get("ran_ue_id", "Unknown")  # Extract ran_ue_id (fallback to "Unknown" if not found)
                    cells = ue.get("cells", [])
                    for cell in cells:
                        # Add current timestamp and ran_ue_id to each cell's data
                        cell_with_metadata = {
                            "timestamp": current_timestamp,
                            "ran_ue_id": ran_ue_id,  # Include the ran_ue_id
                            **cell
                        }

                        # Write header only once if file is empty
                        if not header_written and file.tell() == 0:
                            csv_writer.writerow(cell_with_metadata.keys())  # Write the header row
                            header_written = True
                        csv_writer.writerow(cell_with_metadata.values())  # Write the data row

                # Exit the loop if the "message" field is not "ready"
                if parsed_message.get("message") != "ready":
                    break

    print(f"Data written to {csv_file}")

    # Close the WebSocket connection
    ws.close()
    print("Connection closed")

if __name__ == "__main__":
    while True:
        main()
        print("Waiting before the next iteration...")
        time.sleep(0.5)  # Adjust the delay as needed
