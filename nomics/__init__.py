name = "nomics-python"

import json

from nomics.api import (
    Candles,
    Currencies,
    ExchangeRates,
    Markets,
    Volume
)

class Nomics:
    def __init__(self, key):
        self.key = key

        self.Candles = Candles(self)
        self.Currencies = Currencies(self)
        self.ExchangeRates = ExchangeRates(self)
        self.Markets = Markets(self)
        self.Volume = Volume(self)

    def get_url(self, endpoint):
        return "https://api.nomics.com/v1/{}?key={}".format(endpoint, self.key)

