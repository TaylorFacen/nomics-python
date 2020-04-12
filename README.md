# nomics-python
A Python wrapper for the [Nomics Crypto Market Data API](http://docs.nomics.com/).  For some context, Nomics is a [crypto market cap and pricing data provider](https://nomics.com).

## Disclaimer
Although the api call descriptions are from the official documentation, this is an unofficial API wrapper. 

## Getting Started
Before using the Nomics API, sign up for a [free API key here](https://p.nomics.com/cryptocurrency-bitcoin-api).

To install the wrapper, enter the following into the terminal.
```bash
pip install nomics-python
```

Every api call requires this api key. Make sure to use this key when getting started. 
```python
from nomics import Nomics
nomics = Nomics("This-Is-A-Fake-Key-123")

markets = nomics.Markets.get_markets(exchange = 'binance')
```

## Wrapper Wiki
More information on all of the different API methods are available on the Github wiki page [here](https://github.com/TaylorFacen/nomics-python/wiki).

## Contributing
This project is open for contributions! Teamwork makes the dream work.

