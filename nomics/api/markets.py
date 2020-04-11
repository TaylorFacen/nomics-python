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

    def get_market_cap_history(self, start, end = None):
        '''
        Returns the total market cap for all cryptoassets at intervals between the requested time period.

        :param  str start:  Start time of the interval in RFC3339 format

        :param  str end:    End time of the interval in RFC3339 format. If not provided, the current time is used.  
        '''

        url = self.client.get_url('market-cap/history')
        params = {
            'start': start,
            'end': end
        }
        
        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_exchange_markets_ticker(self, interval = None, currency = None, base = None, quote = None, exchange = None, market = None, convert = None):
        '''
        Returns high level information about individual markets on exchanges integrated with Nomics.

        :param  [str]   interval:   Comma separated time interval of the ticker(s). 
                                    Default is 1d,7d,30d,365d,ytd

        :param  [str]   currency:   A comma separated list of Nomics Currency IDs.

        :param  [str]   base:       A comma separated list of Nomics Currency IDs.

        :param  [str]   quote:      A comma separated list of Nomics Currency IDs. 

        :param  [str]   exchange:   A comma separated list of Nomics Exchange IDs.

        :param  [str]   market:     A comma separated list of Nomics Market IDs.

        :param  str     convert:    Nomics Currency ID to convert all financial data to     
        '''

        url = self.client.get_url('exchange-markets/ticker')
        params = {
            'interval': interval,
            'currency': currency,
            'base': base,
            'quote': quote,
            'exchange': exchange,
            'market': market,
            'convert': convert
        }
        
        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text
