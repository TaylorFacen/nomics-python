import requests
from datetime import datetime

def get_candles(key, interval, exchange = None, market = None, currency = None, start = None, end = None):
    """Returns open, high, low, close, and volume information for Nomics currencies. If the exchange parameter is omitted, all markets where the given currency is the base currency and the quote currency is a fiat currency, BTC, or ETH are returnd. If the exchance parameter is includes, then then the open, high, low, close, and volume for the specified currency is returned only for that exchange.

    Aggregated Candles
    
    Required parameters:
        - interval: Time interval of the candle
        Enum: "1d", "4h", "1h", "30m", "5m", "1m"

        - currency: Currency ID
        Example: "BTC"

    Exchange Candles

    Required parameters:
        - interval: Time interval of the candle
        Enum: "1d", "4h", "1h", "30m", "5m", "1m"

        - exchange: Exchange ID
        Example: "binance"

        - market: Market ID
        Example: "BTCUSDT"

    Both Aggregated and Exchange Candles

    Optional parameters:
        - start: Start time of the interval in isoformat
        Example: "2018-01-01"

        - end: End time of the interval in isoformat
        Example: "2018-01-03"
    """
    if exchange:
        if not market:
            raise TypeError("Missing required argument: 'market'") 
        else:
            url = "https://api.nomics.com/v1/exchange_candles?key={}&interval={}&exchange={}&market={}".format(key, interval, exchange, market)
    else:
        if not currency:
            raise TypeError("Missing required argument: 'currency'")
        else:
            url = "https://api.nomics.com/v1/candles?key={}&interval={}&currency={}".format(key, interval, currency)
            
    if start:
        start_formatted = datetime.strptime(start, '%Y-%m-%d').strftime("%FT%TZ").replace(':', '%3A')
        url += "&start={}".format(start_formatted)
                
    if end:
        end_formatted = datetime.strptime(end, '%Y-%m-%d').strftime("%FT%TZ").replace(':', '%3A')
        url += "&end={}".format(end_formatted)

    r = requests.get(url)
    
    if r.status_code == 200:
        return r.json()
    else:
        return r.text