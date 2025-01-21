# test_funktionen.py
import pytest
from funktionen import addiere, subtrahiere, multipliziere, dividiere

def test_addiere():
    assert addiere(2, 3) == 5
    assert addiere(-1, 1) == 0
    assert addiere(0, 0) == 0

def test_subtrahiere():
    assert subtrahiere(5, 2) == 3
    assert subtrahiere(2, 5) == -3
    assert subtrahiere(0, 0) == 0

def test_multipliziere():
    assert multipliziere(2, 3) == 6
    assert multipliziere(-1, 5) == -5
    assert multipliziere(0, 10) == 0

def test_dividiere():
    assert dividiere(6, 2) == 3
    assert dividiere(5, 2) == 2.5
    with pytest.raises(ZeroDivisionError):
        dividiere(5, 0)