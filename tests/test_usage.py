import logging
import pytest

from config import NOMICS_API_KEY
from nomics import Nomics

@pytest.fixture
def nomics():
    return Nomics(NOMICS_API_KEY)

def test_API_History(nomics):
    data = nomics.Usage.API_History(start = "2022-04-14T00:00:00Z", end = "2022-04-20T00:00:00Z")
    assert isinstance(data, list)
    assert len(data) > 0

def test_API_Summary(nomics):
    data = nomics.Usage.API_Summary()
    assert isinstance(data, dict)
    assert len(data) > 0