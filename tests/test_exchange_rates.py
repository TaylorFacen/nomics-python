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