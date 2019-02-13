import requests
import json

from .currencies import get_currencies, get_prices
from .markets import get_markets, get_market_cap_history, get_dashboard
from .candles import get_candles

class Nomics:
    
    def __init__(self, key):
        self.key = key

    def get_url(self, endpoint):
        return "https://api.nomics.com/v1/{}?key={}".format(endpoint, self.key)

    # Currencies

    def get_currencies(self):
        url = self.get_url('currencies')
        return get_currencies(url)
    
    def get_prices(self):
        url = self.get_url('prices')
        return get_prices(url)

    # Markets
    def get_markets(self, **kwargs):
        url = self.get_url('markets')
        return get_markets(url, **kwargs)

    def get_market_cap_history(self, start, **kwargs):
        url = self.get_url('market-cap/history')
        return get_market_cap_history(url, start, **kwargs)

    def get_dashboard(self):
        url = self.get_url('dashboard')
        return get_dashboard(url)
    
    # Candles
    def get_candles(self, interval, **kwargs):
        if 'exchange' in kwargs.keys():
            url = self.get_url('exchange_candles')
        else:
            url = self.get_url('candles')
        return get_candles(url, interval, **kwargs)