import json

from nomics.api import (
    Currencies
)

class Nomics:
    def __init__(self, key):
        self.key = key

        self.Currencies = Currencies(self)
    
    def get_url(self, endpoint):
        return "https://api.nomics.com/v1/{}?key={}".format(endpoint, self.key)