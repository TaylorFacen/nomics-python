import pytest

from config import NOMICS_API_KEY
from nomics import Nomics

@pytest.fixture
def nomics():
    return Nomics(NOMICS_API_KEY)

def test_get_url(nomics):
    assert nomics.get_url('currencies') == "https://api.nomics.com/v1/currencies?key={}".format(NOMICS_API_KEY)


