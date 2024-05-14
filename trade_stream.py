import os
from alpaca.trading.stream import TradingStream

api_key = os.getenv("TRADE_API_KEY")
secret_key = os.getenv("TRADE_API_SECRET")

trade_stream_client = TradingStream(api_key=api_key, secret_key=secret_key, paper=True)

async def trade_updates_handler(data):
    print(data)
    
    
trade_stream_client.subscribe_trade_updates(trade_updates_handler)
trade_stream_client.run()