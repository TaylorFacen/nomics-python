import requests

from .api import API

class Candles(API):
    def get_candles(self, interval, base, quote = None, exchange = None, start = None, end = None, format = None):
        '''
        Returns aggregated open, high, low, close, and volume information for Nomics currencies. 
        If only base is provided then OHLCV values are returned in USD. 
        If both base and quote are provided, then OHLC values are returned in the quote currency and volume is returned in base currency. 
        If exchange is provided, candles are provided for only that exchange.

        :param  str interval:   Time interval of the candle

        :param  str base:       Base currency of the pair 

        :param  str quote:      Quote currency of the pair   

        :param  str exchange:   Exchange ID 

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

        if exchange:
            url = self.client.get_url('exchange_candles')
            params['exchange'] = exchange
            params['market'] = base + quote

        elif base and quote:
            url = self.client.get_url('markets/candles')
            params['base'] = base
            params['quote'] = quote

        else:
            url = self.client.get_url('candles')
            params['currency'] = base

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text