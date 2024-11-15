# main.py
from ws_operator.stock_operator import startServer

def main():
   try:
        startServer()
       
   except Exception as e:
       print(f"Error in main: {str(e)}")
       raise

if __name__ == "__main__":
   main()