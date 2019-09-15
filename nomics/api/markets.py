import requests

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