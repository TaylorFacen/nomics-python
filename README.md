# nomics-python
A Python wrapper for the [Nomics API](http://docs.nomics.com/)

## Disclaimer
Although the api call descriptions are from the official documentation, this is an unofficial API wrapper. 


## Getting Started
Before using the Nomics API, sign up for a free API key [here](https://p.nomics.com/cryptocurrency-bitcoin-api).

Every api call requires this api key. Make sure to use this key when getting started. 
```
import nomics
api_key = "This-Is-A-Fake-Key-123"
nomics = nomics.Nomics(api_key)
```

## Sample Calls
Here are a few calls that this package provides. For more detailed information, please see the associated Nomics API documentation. 

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