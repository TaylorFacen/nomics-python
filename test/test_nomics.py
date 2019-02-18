from pytest import fixture
from pytest import raises

@fixture
def nomics():
    # Note; This is a test API key. Not to be used for personal use

    api_key = '408cc5e9c771ca59fce4f0f27457a24a'
    import os, os.path
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
    from nomics import Nomics
    return Nomics(api_key)

def test_get_currencies(nomics):
    assert isinstance(nomics.get_currencies(), list)

def test_get_prices(nomics):
    response = nomics.get_prices()
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("currency","price"))

def test_get_all_time_highs(nomics):
    response = nomics.get_all_time_highs()
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("currency","price", "timestamp", "exchange", "quote"))

def test_get_supplies_interval(nomics):
    # Test Case: User only supplies start parameter
    response = nomics.get_supplies_interval(start = '2018-01-01')
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("currency","open_available", "open_max", "open_timestamp", "close_available", "close_max", "close_timestamp"))
    
    # Test Case: User supplies both start and end parameter
    response = nomics.get_supplies_interval(start = '2018-01-01', end = '2018-01-02')
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("currency","open_available", "open_max", "open_timestamp", "close_available", "close_max", "close_timestamp"))

def test_get_currencies_interval(nomics):
    # Test Case: User only supplies start argument
    response = nomics.get_currencies_interval(start = '2018-01-01')
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("currency","volume", "open", "open_timestamp", "close", "close_timestamp"))
    
    # Test Case: User supplies both start and end parameter
    response = nomics.get_currencies_interval(start = '2018-01-01', end = '2018-01-02')
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("currency","volume", "open", "open_timestamp", "close", "close_timestamp"))

def test_get_markets(nomics):
    # Test Case: User doesn't enter any arguments
    response = nomics.get_markets()
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("exchange", "market", "base", "quote"))

    # Test Case: User supplies all optional arguments
    response = nomics.get_markets(exchange = "binance", base = "BTC,ETH,LTC,XMR", quote = "BTC,ETH,BNB")
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("exchange", "market", "base", "quote"))

def test_get_market_cap_history(nomics):
    # Test Case: User only supplies start argument
    response = nomics.get_market_cap_history(start = '2018-01-01')
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("timestamp", "market_cap"))

    # Test Case: User supplies both start and end parameter
    response = nomics.get_market_cap_history(start = '2018-01-01', end = '2018-01-02')
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("timestamp", "market_cap"))

def test_get_dashboard(nomics):
    response = nomics.get_dashboard()
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("currency", "dayOpen", "dayVolume", "dayOpenVolume", 
    "weekOpen", "weekVolume", "weekOpenVolume", 
    "monthOpen", "monthVolume", "monthOpenVolume", 
    "yearOpen", "yearVolume", "yearOpenVolume", 
    "close", "high", "highTimestamp", "highExchange", "highQuoteCurrency", 
    "availableSupply", "maxSupply"))

def test_get_exchange_candles(nomics):
    # Test Case: User only supplies required arguments
    response = nomics.get_candles(interval = "1d", exchange = "binance", market = "BTCUSDT")
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("timestamp", "low", "open", "close", "high", "volume", "num_trades"))
    # Test Case: User supplies all arguments
    response = nomics.get_candles(interval = "1d", exchange = "binance", market = "BTCUSDT", start = "2018-01-01", end = "2018-01-03")
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("timestamp", "low", "open", "close", "high", "volume", "num_trades"))

    # Test Case: User doesn't supply market parameter
    # Should raise TypeError
    with raises(TypeError) as e:
        response = nomics.get_candles(interval = "1d", exchange = "binance", start = "2018-01-01", end = "2018-01-03")

def test_get_aggregated_candles(nomics):
    # Test Case: User only supplies required arguments
    response = nomics.get_candles(interval = "1d", currency = "BTC")
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("timestamp", "low", "open", "close", "high", "volume"))
    # Test Case: User supplies all arguments
    response = nomics.get_candles(interval = "1d", currency = "BTC", start = "2018-01-01", end = "2018-01-03")
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert all (key in response[0] for key in ("timestamp", "low", "open", "close", "high", "volume"))

    # Test Case: User doesn't supply currency parameter
    # Should raise TypeError
    with raises(TypeError) as e:
        response = nomics.get_candles(interval = "1d", start = "2018-01-01", end = "2018-01-03")