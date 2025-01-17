import json
import csv
from websocket import create_connection

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
    csv_file = "output.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
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

                # Flatten the entire JSON response
                flat_message = flatten_json(parsed_message)

                # Write to the CSV file
                if not header_written:
                    # Write the header row from the flattened JSON keys
                    csv_writer.writerow(flat_message.keys())
                    header_written = True

                # Write the data row
                csv_writer.writerow(flat_message.values())

                # Exit the loop if the "message" field is not "ready"
                if parsed_message.get("message") != "ready":
                    break

    print(f"Data written to {csv_file}")

    # Close the WebSocket connection
    ws.close()
    print("Connection closed")

def flatten_json(json_obj, prefix=""):
    """
    Flattens a nested JSON object into a single-level dictionary.
    Keys are prefixed with their parent keys.
    """
    flat_dict = {}
    for key, value in json_obj.items():
        if isinstance(value, dict):
            flat_dict.update(flatten_json(value, prefix + key + "_"))
        else:
            flat_dict[prefix + key] = value
    return flat_dict

if __name__ == "__main__":
    main()
