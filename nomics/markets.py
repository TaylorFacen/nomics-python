import requests
from datetime import datetime

def get_markets(key, exchange = None, base = None, quote = None):
    """Returns information on the exchanges and markets that Nomics supports, in addition to the Nomics currency identifiers for the base and quote currency
    
    Optional parameters:
        - exchange: Nomics exchange ID to filter by
        Example: "binance"

        - base: Comma separated list of base currencies to filter by
        Example: "BTC,ETH,LTC,XMR"

        - quote: Comma separated list of quote currencies to filter by
        Example "BTC,ETH,BNB"

    """
    url = "https://api.nomics.com/v1/markets?key={}".format(key)
    if exchange:
        url += "&exchange={}".format(exchange)
    if base:
        url += "&base={}".format(base)
    if quote:
        url += "&quote={}".format(quote)

    r = requests.get(url)
    
    if r.status_code == 200:
        return r.json()
    else:
        return r.text

def get_market_cap_history(key, start, end = None):
    """Returns information on the exchanges and markets that Nomics supports, in addition to the Nomics currency identifiers for the base and quote currency
    
    Required parameter:
        - start: Start time of the interval in isoformat
        Example: "2018-01-01"

    Optional parameters:
        - end: End time of the interval in isoformat
        Example: "2018-01-03"

    """
    start_formatted = datetime.strptime(start, '%Y-%m-%d').strftime("%FT%TZ").replace(':', '%3A')

    url = "https://api.nomics.com/v1/market-cap/history?key={}&start={}".format(key, start_formatted)
    
    if end:
        end_formatted = datetime.strptime(end, '%Y-%m-%d').strftime("%FT%TZ").replace(':', '%3A')

        url += "&end={}".format(end_formatted)

    r = requests.get(url)
    
    if r.status_code == 200:
        return r.json()
    else:
        return r.text
        
def get_dashboard(key):
    """Returns a high level view of the current state of the market."""
    url = "https://api.nomics.com/v1/dashboard?key={}".format(key)

    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return r.text
