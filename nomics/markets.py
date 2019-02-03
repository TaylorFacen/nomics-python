import requests

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