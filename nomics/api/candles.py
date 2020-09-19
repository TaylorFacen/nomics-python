import requests

from .api import API

class Candles(API):
    def get_candles(self, interval, currency = None, base = None, quote = None, exchange = None, market = None, start = None, end = None, format = None):
        '''
        Returns aggregated open, high, low, close, and volume information for Nomics currencies. 
        If only currency is provided then OHLCV values are returned in USD. 
        If both exchange and market are provided, then Exchange OHLCV candles are returned. 
        If both base and quote are provided, then aggregated OHLCV candles are returned.

        :param  str interval:   Time interval of the candle

        :param  str currency:   Currency 

        :param  str base:       Base currency of the pair 

        :param  str quote:      Quote currency of the pair   

        :param  str exchange:   Exchange ID 

        :param  str market:     The Exchange's Market ID

        :param  str start:      Start time of the interval in RFC3339 format

        :param  str end:        End time of the interval in RFC3339 format.

        :param  str format:     Format of the response. Defaults to JSON when blank.   

        '''

        params = {
            'interval': interval,
            'start': start,
            'end': end,
            'format': format
        }

        if exchange and market:
            url = self.client.get_url('exchange_candles')
            params['exchange'] = exchange
            params['market'] = market

        elif base and quote:
            url = self.client.get_url('markets/candles')
            params['base'] = base
            params['quote'] = quote

        elif currency:
            url = self.client.get_url('candles')
            params['currency'] = currency
        else:
            raise ValueError("Must provide exchange and market, base and quote, or currency")

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text