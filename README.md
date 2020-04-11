# nomics-python
A Python wrapper for the [Nomics Crypto Market Data API](http://docs.nomics.com/).  For some context, Nomics is a [crypto market cap and pricing data provider](https://nomics.com).

## Disclaimer
Although the api call descriptions are from the official documentation, this is an unofficial API wrapper. 

## Contents
* [Getting Started](#getting-started)

## Getting Started
Before using the Nomics API, sign up for a [free API key here](https://p.nomics.com/cryptocurrency-bitcoin-api).

Every api call requires this api key. Make sure to use this key when getting started. 
```python
import nomics
nomics = nomics.Nomics("This-Is-A-Fake-Key-123")
```