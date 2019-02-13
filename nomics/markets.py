import requests
from datetime import datetime

def get_markets(url, exchange = None, base = None, quote = None):
    """Returns information on the exchanges and markets that Nomics supports, in addition to the Nomics currency identifiers for the base and quote currency
    
    Optional parameters:
        - exchange: Nomics exchange ID to filter by
        Example: "binance"

        - base: Comma separated list of base currencies to filter by
        Example: "BTC,ETH,LTC,XMR"

        - quote: Comma separated list of quote currencies to filter by
        Example "BTC,ETH,BNB"

    """

    # API call parameters
    params = {
        'exchange': exchange,
        'base': base,
        'quote': quote
    }

    r = requests.get(url, params = params)
    
    if r.status_code == 200:
        return r.json()
    else:
        return r.text

def get_market_cap_history(url, start, end = None):
    """Returns information on the exchanges and markets that Nomics supports, in addition to the Nomics currency identifiers for the base and quote currency
    
    Required parameter:
        - start: Start time of the interval in isoformat
        Example: "2018-01-01"

    Optional parameters:
        - end: End time of the interval in isoformat
        Example: "2018-01-03"

    """
    
    # API Call paramters
    params = {
        'start': datetime.strptime(start, '%Y-%m-%d').strftime("%FT%TZ")
    }
    if end:
        params['end'] = datetime.strptime(end, '%Y-%m-%d').strftime("%FT%TZ")

    r = requests.get(url, params = params)
    
    if r.status_code == 200:
        return r.json()
    else:
        return r.text
        
def get_dashboard(url):
    """Returns a high level view of the current state of the market."""

    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return r.text
