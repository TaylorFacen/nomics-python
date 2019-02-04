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
api_key = "This-Is-A-Fake-Key-123"
nomics = nomics.Nomics(api_key)
```

## Code Examples
Here are a few calls that this package provides. For more detailed information, please see the associated Nomics API documentation. 

* [Prices](#prices)
  * get_currencies
  * get_prices
* [Markets](#markets)
  * get_markets
  * get_market_cap_history
  * get_dashboard
* [Candles](#candles)
  * get_candles


### Prices

* [get_currencies](http://docs.nomics.com/#tag/Currencies) - Returns a list of all of the currency Ids

Input

No parameters
```
nomics.get_currencies()
```
Output
```
['0XBTC', '1ST', '2GIVE', '3DES', 'ABA'...]
```

* [get_prices](http://docs.nomics.com/#operation/getPrices) - Returns current prices for all currencies

Input

No parameters
```
nomics.get_prices()
```

Output
```
[
    {
        'currency': 'BTC', 
        'price': '3438.52345'
    }, {
        'currency': 'BTCP', 
        'price': '0.86186'
    }
    ...
]
```

### Markets

* [get_markets](http://docs.nomics.com/#operation/getMarkets) - Returns information on the exchanges and markets that Nomics supports, in addition to the Nomics currency identifiers for the base and quote currency.

Input

Optional Parameters:
* exchange: Nomics exchange ID to filter by
* base: Comma separated list of base currencies to filter by
* quote: Comma separated list of quote currencies to filter by
```
nomics.get_markets(exchange = "binance", base = "BTC,ETH,LTC,XMR", quote = "BTC,ETH,BNB")
```
Output
```
[
    {
        'exchange': 'binance', 
        'market': 'ETHBTC', 
        'base': 'ETH', 
        'quote': 'BTC'
    }, {
        'exchange': 'binance', 
        'market': 'LTCBTC', 
        'base': 'LTC', 
        'quote': 'BTC'
    }, ...
]
```


* [get_market_cap_history](http://docs.nomics.com/#operation/getMarketCapHistory) - Returns the total market cap for all cryptoassets at intervals between the requested time period.

Input

Required Parameters:
* start: Start time of the interval in isoformat

Optional Parameters:
* end: End time of the interval in isoformat
```
nomics.get_market_cap_history(start = '2019-01-01', end = '2019-01-03')
```
Output
```
[
    {
        'timestamp': '2019-01-01T00:00:00Z', 
        'market_cap': '129069743869'
    }, {
        'timestamp': '2019-01-02T00:00:00Z', 
        'market_cap': '133550203583'
    }, {
        'timestamp': '2019-01-03T00:00:00Z', 
        'market_cap': '128268414469'}
]
```

* [get_dashboard](http://docs.nomics.com/#operation/getDashboard) - Returns a high level view of the current state of the market.

Input

No parameters
```
nomics.get_dashboard()
```
Output
```
[
    ... {
        'currency': 'BTC', 
        'dayOpen': '3511.99577900', 
        'dayVolume': '99792173.77561706', 
        'dayOpenVolume': '110587082.15678930', 
        'weekOpen': '3456.85794661', 
        'weekVolume': '1239234754.79406981', 
        'weekOpenVolume': '1148015971.33757139', 
        'monthOpen': '3858.41231750', 
        'monthVolume': '6443576407.76799557', 
        'monthOpenVolume': '11701713847.30718734', 
        'yearOpen': '8164.13564882', 
        'yearVolume': '234521217323.90533474', 
        'yearOpenVolume': '324699677804.24397743', 
        'close': '3454.32472322', 
        'high': '24436.29525153', 
        'highTimestamp': '2018-01-05T00:00:00Z', 
        'highExchange': 'bithumb', 
        'highQuoteCurrency': 'KRW', 
        'availableSupply': '17517750', 
        'maxSupply': '21000000'
    }, ...
]
```


### Candles
* get_candles - Combines the [Aggregated OHLCV](http://docs.nomics.com/#operation/getCandles) and [Exchange OHLCV](http://docs.nomics.com/#operation/getExchangeCandles) APIs.

Aggregated Candles

Input

Required Parameters:
* interval: Time interval of the candle (Has to be one of the following values: "1d", "4h", "1h", "30m", "5m", "1m")
* currency: Currency ID

Optional Parameters:
* start: Start time of the interval in isoformat
* end: End time of the interval in isoformat
```
nomics.get_candles(interval = "1d", currency = "BTC", start = "2018-01-01", end = "2018-01-03")
```
Output
```
[
    {
        'timestamp': '2018-01-01T00:00:00Z', 
        'low': '13493.21831', 
        'open': '14071.16898', 
        'close': '13549.53608', 
        'high': '13793.07961', 
        'volume': '1490453543'
    }, {
        'timestamp': '2018-01-02T00:00:00Z', 
        'low': '14421.69036', 
        'open': '14275.23107', 
        'close': '14789.29684', 
        'high': '14416.79422', 
        'volume': '3048511009'
    }, ...
]
```

Exchange Candles

Input

Required Parameters:
* interval: Time interval of the candle (Has to be one of the following values: "1d", "4h", "1h", "30m", "5m", "1m")
* exchange: Exchange ID
* market: Market ID

Optional Parameters:
* start: Start time of the interval in isoformat
* end: End time of the interval in isoformat
```
nomics.get_candles(interval = "1d", exchange = "binance", market = "BTCUSDT", start = "2018-01-01", end = "2018-01-03")
```
Output
```
[
    {
        'timestamp': '2018-01-01T00:00:00Z', 
        'low': '12750.00000000', 
        'open': '13715.65000000', 
        'close': '13380.00000000', 
        'high': '13818.55000000', 
        'volume': '8609.91584400', 
        'num_trades': '99182'
    }, {
        'timestamp': '2018-01-02T00:00:00Z', 
        'low': '12890.02000000', 
        'open': '13382.16000000', 
        'close': '14675.11000000', 
        'high': '15473.49000000', 
        'volume': '20078.09211100', 
        'num_trades': '165673'
    }, ...
]
```
