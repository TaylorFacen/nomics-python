import requests

from .api import API
from .service import format_date

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

    def get_history(self, currency, start, end = None):
        '''
        Returns exchange rates for every point in a time range.

        :param  str     currency:   Currency ID

        :param  str     start:      Start time of the interval in ISO or RFC3339 format

        :param  str     end:        End time of the interval in ISO or RFC3339 format. If not provided, the current time is used. 
        '''

        url = self.client.get_url('exchange-rates/history')
        params = {
            'currency': currency,
            'start': format_date(start)
        }

        if end:
            params['end'] = format_date(end)

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_interval(self, start, end = None):
        '''
        Returns exchange rates for every point in a time range.

        :param  str     start:      Start time of the interval in ISO or RFC3339 format

        :param  str     end:        End time of the interval in ISO or RFC3339 format. If not provided, the current time is used. 
        '''

        url = self.client.get_url('exchange-rates/interval')
        params = {
            'start': format_date(start)
        }

        if end:
            params['end'] = format_date(end)

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text



