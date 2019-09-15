import logging
import pytest

from config import NOMICS_API_KEY
from nomics import Nomics

@pytest.fixture
def nomics():
    return Nomics(NOMICS_API_KEY)

def test_get_exchange_rates(nomics):
    data = nomics.ExchangeRates.get_exchange_rates()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_history(nomics):
    data = nomics.ExchangeRates.get_history(
        currency = "ETH",
        start = "2018-04-14T00:00:00Z"
    )
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_interval(nomics):
    data = nomics.ExchangeRates.get_interval(
        start = "2018-04-14T00:00:00Z"
    )
    assert isinstance(data, list)
    assert len(data) > 0