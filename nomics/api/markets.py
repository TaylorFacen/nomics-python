import requests
from .service import format_date

from .api import API

class Markets(API):
    def get_markets(self, exchange = None, base = None, quote = None):
        '''
        Returns information on the exchanges and markets that Nomics supports

        :param  str     exchange:   Nomics Exchange ID to filter by
                                    Optional   

        :param  [str]   base:       Comma separated list of base currencies to filter by
                                    Optional

        :param  [str]   quote:      Comma separated list of quote currencies to filter by 
                                    Optional   
        '''

        url = self.client.get_url('markets')
        params = {
            'exchange': exchange,
            'base': base,
            'quote': quote
        }

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_market_cap_history(self, start, end = None):
        '''
        Returns the total market cap for all cryptoassets at intervals between the requested time period.

        :param  str start:  Start time of the interval in ISO or RFC3339 format

        :param  str end:    End time of the interval in ISO or RFC3339 format. If not provided, the current time is used.  
        '''

        url = self.client.get_url('market-cap/history')
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