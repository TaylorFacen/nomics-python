import requests

from .api import API


class Usage(API):
    def API_History(self, start=None, end=None):
        """
        Returns historical API usage data for metered API keys.

        :param  [str]   start:      Start time in IS8601 format.
                                    Optional

        :param  [str]   end:        End time in IS8601 format. At most 30 days past start.
                                    Optional

        """

        url = self.client.get_url("meta/usage")
        if (start and end) == None:
            params = {
                "start": start,
                "end": end,
            }
        else:
            params = {
            }

        resp = requests.get(url, params=params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text

    def API_Summary(self):
        """
        Returns summary of the API calls made during the current billing period.

        """

        url = self.client.get_url("meta/overage")
        params = {
        }

        resp = requests.get(url, params=params)

        if resp.status_code == 200:
            return resp.json()
        else:
            return resp.text
