import json
import pandas as pd
import os
from datetime import datetime
from config.createfile import createCSVFile;

def writeDataInCSV (message):
    try:
        # Parse JSON message
        data = json.loads(message)
        if 'data' in data:
            print("Trade Data:", data['data'])
            file_exists = os.path.exists('stock_data.csv') #stored data file path

            if not file_exists:
                createCSVFile(message)

            else:            
                # Create new data list
                new_data = []
                for trade in data['data']:
                    timestamp = datetime.fromtimestamp(trade['t']/1000).strftime('%Y-%m-%d %H:%M:%S')
                    new_data.append([timestamp, trade['s'], trade['p'], trade['v']])

                # Convert to DataFrame
                new_df = pd.DataFrame(new_data, columns=['timestamp', 'symbol', 'price', 'volume'])

                try:
                    # Read existing CSV if it exists
                    existing_df = pd.read_csv('stock_data.csv')
                    combined_df = pd.concat([existing_df, new_df], ignore_index=True)
                except FileNotFoundError:
                    combined_df = new_df

                # Save combined data
                combined_df.to_csv('stock_data.csv', index=False)
                print('Data appended successfully')

                # Pretty print the data
                print(json.dumps(data['data'], indent=2))
            
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Error processing message: {e}")
