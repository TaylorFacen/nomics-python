# nomics-python
A Python wrapper for the [Nomics API](http://docs.nomics.com/)


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

* [get_currencies](http://docs.nomics.com/#tag/Currencies) - Returns a list of all of the currency Ids
```
nomics.get_currencies()
```

* [get_prices](http://docs.nomics.com/#operation/getPrices) - Returns current prices for all currencies
```
nomics.get_prices()
```
