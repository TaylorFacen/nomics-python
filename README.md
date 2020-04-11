# nomics-python
A Python wrapper for the [Nomics Crypto Market Data API](http://docs.nomics.com/).  For some context, Nomics is a [crypto market cap and pricing data provider](https://nomics.com).

## Disclaimer
Although the api call descriptions are from the official documentation, this is an unofficial API wrapper. 

## Contents
* [Getting Started](#getting-started)
* [API Methods](#api-methods)

## Getting Started
Before using the Nomics API, sign up for a [free API key here](https://p.nomics.com/cryptocurrency-bitcoin-api).

Every api call requires this api key. Make sure to use this key when getting started. 
```python
import nomics
nomics = nomics.Nomics("This-Is-A-Fake-Key-123")
```

## API Methods
The following is a list of all supported API methods. For more information, please see the associated Nomics documentation.

* [Currencies](#currencies)
    * get_currencies

### Currencies
[get_currencies](https://docs.nomics.com/#operation/getCurrenciesTicker) - Price, volume, market cap, and rank for all currencies across 1 hour, 1 day, 7 day, 30 day, 365 day, and year to date intervals. Current prices are updated every 10 seconds.

```python
# Required arguments
nomics.Currencies.get_currencies(ids = ['BTC'])

# All arguments
nomics.Currencies.get_currencies(
    ids = ["BTC", "ETH"],
    interval = ["1d", "ytd"],
    convert = "EUR",
    include_transparency = True
)
```

[get_metadata](https://docs.nomics.com/#operation/getCurrencies) - The currencies endpoint returns all the currencies and their metadata that Nomics supports.
```python
# Required arguments
nomics.Currencies.get_metadata()

# All arguments
nomics.Currencies.get_metadata(
    ids = ["BTC", "ETH"],
    attributes = ["id", "name", "logo_url"]
)
```

[get_sparkline](https://docs.nomics.com/#operation/getCurrenciesSparkline) - The currencies sparkline endpoint returns prices for all currencies within a customizable time interval suitable for sparkline charts.

```python
# Required arguments
nomics.Currencies.get_sparkline(
    start = "2018-04-14T00:00:00Z"
)

# All arguments
nomics.Currencies.get_sparkline(
    start = "2018-04-14T00:00:00Z",
    end = "2018-06-14T00:00:00Z"
)
```
