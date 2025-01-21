# test_benutzer.py
import pytest
from benutzer import Benutzer

def test_benutzer_gueltig():
    benutzer = Benutzer("Max", 30)
    assert benutzer.name == "Max"
    assert benutzer.alter == 30

def test_benutzer_ungueltiger_name():
    with pytest.raises(TypeError):
        Benutzer(123, 30)

def test_benutzer_ungueltiges_alter():
    with pytest.raises(ValueError):
        Benutzer("Max", -5)