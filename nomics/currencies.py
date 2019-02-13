import requests

def get_currencies(url):
    """Returns a list of Nomics currency IDs"""

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

def get_prices(url):
    """Returns a list of dictionaries of currencies and current price"""

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()
    else:
        return r.text

def get_all_time_highs(url):
    """Returns all time high information for all currencies"""

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()
    else:
        return r.text
