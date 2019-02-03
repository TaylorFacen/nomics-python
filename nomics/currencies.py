import requests

def get_currencies(key):
    """Returns a list of Nomics currency IDs"""

    url = "https://api.nomics.com/v1/currencies?key={}".format(key)
    r = requests.get(url)
    
    if r.status_code == 200:
        # r.json() returns a list of dictionaries 
        # e.g. [{'id': 'XPM'}, {'id': 'XPST'}]
        currency_ids = []
        for item in r.json():
            currency_ids.append(item['id'])
    
        return currency_ids
    else:
        return r.text

def get_prices(key):
        """Returns a list of dictionaries of currencies and current price"""

        url = "https://api.nomics.com/v1/prices?key={}".format(key)
        
        r = requests.get(url)

        if r.status_code == 200:
            return r.json()
        else:
            return r.text