import requests

from .api import API
from .service import format_date

class Volume(API):
    def get_volume_history(self, start = None, end = None):
        '''
        Returns the total volume for all cryptoassets in USD at intervals between the requested time period.

        :param  str start:  Start time of the interval in ISO or RFC3339 format

        :param  str end:    End time of the interval in ISO or RFC3339 format. If not provided, the current time is used.  
        '''

        url = self.client.get_url('volume/history')
        params = {}

        if start:
            params['start'] = format_date(start)

        if end:
            params['end'] = format_date(end)
        
        resp = requests.get(url, params = params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text