# nomics-python
A Python wrapper for the [Nomics API](http://docs.nomics.com/)

## Disclaimer
Although the api call descriptions are from the official documentation, this is an unofficial API wrapper. 

## Contents
* [Getting Started](#getting-started)
* [Code Examples](#code-examples)
* [Change Log](Changelog.md)

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
    * get_metadata
    * get_sparkline
* [ExchangeRates](#ExchangeRates)
    * get_exchange_rates
    * get_history
    * get_interval
* [Markets](#markets)
    * get_markets
* [Volume](#volume)
    * get_volume_history

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

[get_metadata](https://docs.nomics.com/#operation/getCurrencies) - The currencies endpoint returns all the currencies and their metadata that Nomics supports.

Input

Optional Parameters
* ids:  Comma separated list of Nomics Currency IDs to filter result rows.
* attributes: Comma separated list of currency attributes to filter result columns

```
nomics.Currencies.get_metadata(
    ids = ["BTC", "ETH"],
    attributes = ["id", "name", "logo_url"]
)
```

[get_sparkline](https://docs.nomics.com/#operation/getCurrenciesSparkline) - The currencies sparkline endpoint returns prices for all currencies within a customizable time interval suitable for sparkline charts.

Input

Required Parameters
* start: Start time of the interval in ISO or RFC3339 format

Optional Parameters
* end: End time of the interval in ISO or RFC3339 format

```
nomics.Currencies.get_sparkline(
    start = "2018-04-14T00:00:00Z",
    end = "2018-06-14T00:00:00Z"
)
```

### ExchangeRates

[get_exchange_rates](https://docs.nomics.com/#tag/Exchange-Rates) - The exchange rates endpoint returns the current exchange rates used by Nomics to convert prices from markets into USD. This contains Fiat currencies as well as a BTC and ETH quote prices.

```
nomics.ExchangeRates.get_exchange_rates()
```

[get_history](https://docs.nomics.com/#operation/getExchangeRatesHistory) - Exchange rates for every point in a time range. This endpoint can be used with other interval endpoints to convert values into a desired quote currency.

Input

Required Parameters
* currency: Currency ID
* start: Start time of the interval in ISO or RFC3339 format

Optional Parameters
* end: End time of the interval in ISO or RFC3339 format

```
nomics.ExchangeRates.get_history(
    currency = "ETH",
    start = "2018-04-14T00:00:00Z",
    end = "2018-06-14T00:00:00Z"
)
```

[get_interval](https://docs.nomics.com/#operation/getExchangeRatesInterval) - Exchange rates to convert from USD over a time interval.

Input

Required Parameters
* start: Start time of the interval in ISO or RFC3339 format

Optional Parameters
* end: End time of the interval in ISO or RFC3339 format

```
nomics.ExchangeRates.get_interval(
    start = "2018-04-14T00:00:00Z",
    end = "2018-06-14T00:00:00Z"
)
```

### Markets

[get_markets](https://docs.nomics.com/#operation/getMarkets) - The markets endpoint returns information on the exchanges and markets that Nomics supports, in addition to the Nomics currency identifiers for the base and quote currency.

Input

Optional Paramters
* exchange: Nomics Exchange ID to filter by
* base: Comma separated list of base currencies to filter by
* quote: Comma separated list of quote currencies to filter by

```
nomics.Markets.get_markets(
    exchange = "binance",
    base = ["BTC", "ETH", "LTC"],
    quote = ["BNB"]
)
```

[get_market_cap_history](https://docs.nomics.com/#operation/getMarketCapHistory) - MarketCap History is the total market cap for all cryptoassets at intervals between the requested time period.

Input

Required Parameters
* start: Start time of the interval in ISO or RFC3339 format

Optional Parameters
* end: End time of the interval in ISO or RFC3339 format

```
nomics.Markets.get_market_cap_history(
    start = "2018-04-14T00:00:00Z",
    end = "2018-06-14T00:00:00Z"
)
```

### Volume
[get_volume_history](https://docs.nomics.com/#operation/getVolumeHistory) - Volume History is the total volume for all cryptoassets in USD at intervals between the requested time period.

Input

Optional Parameters
* start: Start time of the interval in ISO or RFC3339 format
* end: End time of the interval in ISO or RFC3339 format

```
nomics.Volume.get_volume_history(
    start = "2018-04-14T00:00:00Z",
    end = "2018-06-14T00:00:00Z"
)
```

