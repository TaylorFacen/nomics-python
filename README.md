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
```
nomics.get_currencies()
```
Output
```
['0XBTC', '1ST', '2GIVE', '3DES', 'ABA'...]
```

* [get_prices](http://docs.nomics.com/#operation/getPrices) - Returns current prices for all currencies

Input
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