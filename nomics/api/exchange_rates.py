import requests

from .api import API

class ExchangeRates(API):
    def get_exchange_rates(self, format = None):
        '''
        Returns the current exchange rates used by Nomics to convert prices from markets into USD. 
        This contains Fiat currencies as well as a BTC and ETH quote prices.

        :param  str format: Format of the response. Defaults to JSON when blank.

        '''

        url = self.client.get_url('exchange-rates')
        params = {
            'format': format
        }

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text