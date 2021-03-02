import requests

from .api import API

class Currencies(API):
    def get_currencies(self, ids, interval = None, convert = None, status = None, filter = None, sort = None,
                       include_transparency = False, per_page = None, page = None):
        '''
        Returns price, volume, market cap, and rank for all currencies

        :param  str   ids:                      Comma separated list of Nomics Currency IDs
                                                to filter result rows.

        :param  str   interval:                 Comma separated time interval of the ticker(s).
                                                Default is 1d,7d,30d,365d,ytd

        :param  str   convert:                  Currency to quote ticker price, market cap, and volume values.
                                                May be a Fiat Currency or Cryptocurrency.
                                                Default is USD.

        :param  str   status:                   Status by which to filter currencies. If not provided, all currencies
                                                are shown.
                                                Available options: "active" "inactive" "dead"

        :param  str   filter:                   Further filter the set of currencies. The new filter returns currencies
                                                that have recently been priced by Nomics and any returns currencies
                                                regardless of their state. The any filer may be used to retrieve
                                                new-but-stale currencies that are listed under new, but are no longer
                                                active.
                                                Available options: "any" "new"

        :param  str   sort:                     How to sort the returned currencies. rank sorts by rank ascending and
                                                first_priced_at sorts by when each currency was first priced by Nomics
                                                descending.
                                                Available options: "rank" "first_priced_at"

        :param  bool  include-transparency:     Whether to include Transparent Volume information for currencies.
                                                Default is false. Only available to paid API plans

        :param  int    per_page:                The maximum number of items to return per paginated response

        :param  int    page:                    Which page of items to get. Only applicable when per-page is also
                                                supplied.
        '''

        if type(ids) != str:
            raise ValueError("ids must be a comma separated string. E.g. ids=BTC,ETH,XRP")
        if interval and type(interval) != str:
            raise ValueError("interval must be a comma separated string. E.g. 1d,7d,30d,365d,ytd")


        url = self.client.get_url('currencies/ticker')
        params = {
            'ids': ids,
            'interval': interval,
            'convert': convert,
            'status': status,
            'filter': filter,
            'sort': sort,
            'include-transparency': include_transparency or None,
            'per-page': per_page,
            'page': page
        }

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_metadata(self, ids = None, attributes = None):
        '''
        Returns  all the currencies and their metadata that Nomics supports

        :param  [str]   ids:        Comma separated list of Nomics Currency IDs 
                                    to filter result rows. Optional

        :param  [str]   attributes: Comma separated list of currency attributes to filter result columns
                                    Optional
        '''

        url = self.client.get_url('currencies')
        params = {
            'ids': ids,
            'attributes': attributes
        }

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_sparkline(self, start, end = None):
        '''
        Returns prices for all currencies within a customizable time interval suitable for sparkline charts.

        :param  str start:  Start time of the interval in RFC3339 format

        :param  str end:    End time of the interval in RFC3339 format. If not provided, the current time is used.
        '''

        url = self.client.get_url('currencies/sparkline')
        params = {
            'start': start,
            'end': end
        }

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def get_supplies_interval(self, start, end = None):
        '''
        Returns the open and close suplly information for all currencies between a customizable time interval

        :param  str start:  Start time of the interval in RFC3339 format

        :param  str end:    End time of the interval in RFC3339 format. If not provided, the current time is used.
        '''

        url = self.client.get_url('supplies/interval')
        params = {
            'start': start,
            'end': end
        }

        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text