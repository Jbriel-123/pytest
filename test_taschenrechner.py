# test_taschenrechner.py
import pytest
from taschenrechner import Taschenrechner

@pytest.fixture
def taschenrechner():
    return Taschenrechner()

def test_addiere(taschenrechner):
    assert taschenrechner.addiere(2, 3) == 5

def test_subtrahiere(taschenrechner):
    assert taschenrechner.subtrahiere(5, 2) == 3

def test_multipliziere(taschenrechner):
    assert taschenrechner.multipliziere(2, 3) == 6

def test_dividiere(taschenrechner):
    assert taschenrechner.dividiere(6, 2) == 3
    with pytest.raises(ZeroDivisionError):
        taschenrechner.dividiere(5, 0)