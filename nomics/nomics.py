import requests
import json

class Nomics:
    def __init__(self, key):
        self.key = key

    def get_currencies(self):
        """Returns a list of Nomics currency IDs"""

        url = "https://api.nomics.com/v1/currencies?key={}".format(self.key)
        r = requests.get(url)
        
        if r.status_code == 200:
            # r.json() returns a list of dictionaries 
            # e.g. [{'id': 'XPM'}, {'id': 'XPST'}]
            currency_ids = []
            for item in r.json():
                currency_ids.append(item['id'])
        
            return currency_ids
        else:
            print(r.text)