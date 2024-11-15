import websocket
import os
import json
from dotenv import load_dotenv
from datetime import datetime
import pandas as pd
from config.constants import SUBSCRIPTION_LIST
from config.writedata import writeDataInCSV

load_dotenv()

def on_message(ws, message):
    writeDataInCSV(message)


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
