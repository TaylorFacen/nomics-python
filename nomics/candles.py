import requests
from datetime import datetime

def get_candles(url, interval, exchange = None, market = None, currency = None, start = None, end = None):
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
        if not currency:
            raise TypeError("Missing required argument: 'currency'")


    params = {
        'interval': interval,
        'exchange': exchange,
        'market': market,
        'currency': currency,
    }

    if start:
        params['start'] = datetime.strptime(start, '%Y-%m-%d').strftime("%FT%TZ")
    
    if end:
        params['end'] = datetime.strptime(end, '%Y-%m-%d').strftime("%FT%TZ")

    r = requests.get(url, params = params)
    
    if r.status_code == 200:
        return r.json()
    else:
        return r.text