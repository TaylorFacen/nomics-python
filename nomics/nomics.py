import requests
import json

from .currencies import get_currencies, get_prices

class Nomics:
    

    def __init__(self, key):
        self.key = key

    # Currencies

    def get_currencies(self):
        return get_currencies(self.key)
    
    def get_prices(self):
        return get_prices(self.key)