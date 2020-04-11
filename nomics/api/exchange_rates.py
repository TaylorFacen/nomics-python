import requests

from .api import API

class ExchangeRates(API):
    def get_rates(self, format = None):
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

    def get_history(self, currency, start, end = None):
        '''
        Returns exchange rates for every point in a time range.

        :param  str     currency:   Currency ID

        :param  str     start:      Start time of the interval in RFC3339 format

        :param  str     end:        End time of the interval in RFC3339 format. If not provided, the current time is used. 
        '''

        url = self.client.get_url('exchange-rates/history')
        params = {
            'currency': currency,
            'start': start,
            'end': end
        }

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text