import csv
import os
import json
from datetime import time

def createCSVFile(message):
    try:
       data = json.loads(message)
       if 'data' in data:
            file_exists = os.path.exists('stock_data.csv') #stored data file path
           
            with open('stock_data.csv', 'a', newline='') as f:
               writer = csv.writer(f)

               # Write header only if file is new
               if not file_exists:
                   writer.writerow(['timestamp', 'symbol', 'price', 'volume'])
               
               for trade in data['data']:
                   timestamp = time.strftime('%Y-%m-%d %H:%M:%S', 
                                          time.localtime(trade['t']/1000))
                   row = [timestamp, trade['s'], trade['p'], trade['v']]
                   writer.writerow(row)
                   print(f"Data appended: {row}")
    except Exception as e:
       print(f"Error: {e}")