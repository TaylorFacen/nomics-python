import sys
sys.path.append("..")
from nomics import Nomics

import json
api_key = '408cc5e9c771ca59fce4f0f27457a24a'

nomics = Nomics(api_key)


print(" - Currencies")
response = nomics.get_currencies()
print("Get Currencies: \n", response[:5], "\n")

response = nomics.get_prices()[0]
print("Get Prices: \n", json.dumps(response, indent = 4), "\n")

response = nomics.get_all_time_highs()[1]
print("Get All Time Highs: \n", json.dumps(response, indent = 4), "\n")

response = nomics.get_supplies_interval(start = '2018-01-01')[0]
print("Get Supplies Interval: \n", json.dumps(response, indent = 4), "\n")

response = nomics.get_currencies_interval(start = '2018-01-01')[0]
print("Get Currencies Interval: \n", json.dumps(response, indent = 4), "\n")

response = nomics.get_markets()[0]
print("Get Markets: \n", json.dumps(response, indent = 4), "\n")

response = nomics.get_market_cap_history(start = '2018-01-01')[0]
print("Get Market Cap History: \n", json.dumps(response, indent = 4), "\n")

response = nomics.get_dashboard()[0]
print("Get Dashboard: \n", json.dumps(response, indent = 4), "\n")

response = nomics.get_candles(interval = "1d", exchange = "binance", market = "BTCUSDT", start = "2018-01-01", end = "2018-01-03")[0]
print("Get Exchange Candles: \n", json.dumps(response, indent = 4), "\n")

response = nomics.get_candles(interval = "1d", currency = "BTC", start = "2018-01-01", end = "2018-01-03")[0]
print("Get Aggregated Candles: \n", json.dumps(response, indent = 4), "\n")