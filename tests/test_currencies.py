import pytest

from config import NOMICS_API_KEY
from nomics import Nomics

@pytest.fixture
def nomics():
    return Nomics(NOMICS_API_KEY)

def test_get_currencies(nomics):
    data = nomics.Currencies.get_currencies(ids = "BTC, ETC")
    assert isinstance(data, list)
    assert len(data) == 2

def test_get_currencies_params(nomics):
    with pytest.raises(ValueError):
        data = nomics.Currencies.get_currencies(ids = ["BTC", 'ETC'])

def test_get_metadata(nomics):
    data = nomics.Currencies.get_metadata(ids = ["BTC"])
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_sparkline(nomics):
    data = nomics.Currencies.get_sparkline(start = "2020-04-01T00:00:00Z")
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_supplies_interval(nomics):
    data = nomics.Currencies.get_supplies_interval(start = "2018-04-14T00:00:00Z")
    assert isinstance(data, list)
    assert len(data) > 0