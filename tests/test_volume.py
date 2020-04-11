import logging
import pytest

from config import NOMICS_API_KEY
from nomics import Nomics

@pytest.fixture
def nomics():
    return Nomics(NOMICS_API_KEY)

def test_get_volume_history(nomics):
    data = nomics.Volume.get_volume_history(start = "2018-04-14T00:00:00Z")
    assert isinstance(data, list)
    assert len(data) > 0