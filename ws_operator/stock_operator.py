import websocket
import json
import os
from config.constants import SUBSCRIPTION_LIST

def on_message(ws, message):
    try:
        # Parse JSON message
        data = json.loads(message)
        
        # Print only data part
        if 'data' in data:
            print("Trade Data:", data['data'])
            
            # If you want to print specific fields from data
            for trade in data['data']:
                # print(f"Stcok Name: {trade['s']},Price: {trade['p']}, Volume: {trade['v']}, Time: {trade['t']}")                
                # Or pretty print the data
                print(json.dumps(data['data'], indent=2))
                
            
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"Error processing message: {e}")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    for subscription in SUBSCRIPTION_LIST:
        ws.send(json.dumps(subscription))

def startServer():
    websocket.enableTrace(True)
    token = os.environ['FINNHUB_API_KEY']
    ws = websocket.WebSocketApp(f'wss://ws.finnhub.io?token={token}',
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
