import requests

def get_markets(key, **kwargs):
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
    if 'exchange' in kwargs:
        url += "&exchange={}".format(kwargs['exchange'])
    if 'base' in kwargs:
        url += "&base={}".format(kwargs['base'])
    if 'quote' in kwargs:
        url += "&quote={}".format(kwargs['quote'])

    r = requests.get(url)
    
    if r.status_code == 200:
        return r.json()
    else:
        return r.text