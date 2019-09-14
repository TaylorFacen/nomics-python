# nomics-python
A Python wrapper for the [Nomics API](http://docs.nomics.com/)

## Disclaimer
Although the api call descriptions are from the official documentation, this is an unofficial API wrapper. 

## Contents
* [Getting Started](#getting-started)
* [Code Examples](#code-examples)

## Getting Started
Before using the Nomics API, sign up for a free API key [here](https://p.nomics.com/cryptocurrency-bitcoin-api).

Every api call requires this api key. Make sure to use this key when getting started. 
```
import nomics
nomics = nomics.Nomics("This-Is-A-Fake-Key-123")
```

## Code Examples
Here are a few calls that this package provides. For more detailed information, please see the associated Nomics API documentation. 
* [Currencies](#currencies)
    * get_currencies

### Currencies
[get_currencies](https://docs.nomics.com/#operation/getCurrenciesTicker) - Price, volume, market cap, and rank for all currencies across 1 hour, 1 day, 7 day, 30 day, 365 day, and year to date intervals. Current prices are updated every 10 seconds.

Input

Optional Parameters
* ids:  Comma separated list of Nomics Currency IDs to filter result rows.
* interval: Comma separated time interval of the ticker(s). Default is 1d,7d,30d,365d,ytd
* convert: Currency to quote ticker price, market cap, and volume values. May be a Fiat Currency or Cryptocurrency. Default is USD. 
* include-transparency: Whether to include Transparent Volume information for currencies. Default is false. Only available to paid API plans

```
nomics.Currencies.get_currencies(
    ids = ["BTC", "ETH"],
    interval = ["1d", "ytd"],
    convert = "EUR"
)
```