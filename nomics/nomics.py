import requests
import json

from .currencies import get_currencies, get_prices
from .markets import get_markets, get_market_cap_history, get_dashboard
from .candles import get_candles

class Nomics:
    

    def __init__(self, key):
        self.key = key

    # Currencies

    def get_currencies(self):
        return get_currencies(self.key)
    
    def get_prices(self):
        return get_prices(self.key)

    # Markets
    def get_markets(self, **kwargs):
        return get_markets(self.key, **kwargs)

    def get_market_cap_history(self, start, **kwargs):
        return get_market_cap_history(self.key, start, **kwargs)

    def get_dashboard(self):
        return get_dashboard(self.key)
    
    # Candles
    def get_candles(self, interval, **kwargs):
        return get_candles(self.key, interval, **kwargs)