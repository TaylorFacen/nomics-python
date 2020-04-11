import logging
import pytest

from config import NOMICS_API_KEY
from nomics import Nomics

@pytest.fixture
def nomics():
    return Nomics(NOMICS_API_KEY)

def test_get_markets(nomics):
    data = nomics.Markets.get_markets(exchange = 'binance')
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_market_cap_history(nomics):
    data = nomics.Markets.get_market_cap_history(start = "2018-04-14T00:00:00Z")
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_exchange_markets_ticker(nomics):
    data = nomics.Markets.get_exchange_markets_ticker(exchange = 'binance')
    assert isinstance(data, list)
    assert len(data) > 0