import requests

from .api import API

class ExchangeRates(API):
    def get_exchange_rates(self):
        '''
        Returns the current exchange rates used by Nomics to convert prices from markets into USD. 
        This contains Fiat currencies as well as a BTC and ETH quote prices.
        '''

        url = self.client.get_url('exchange-rates')

        resp = requests.get(url)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text
