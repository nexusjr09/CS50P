import pytest 
from numb3rs import validate

def test_valid_addresses():
    assert validate("12.56.78.99") == True
    assert validate("23.46.1.4") == True
    assert validate("45.67.89.1") == True

def test_invalid_adresses():
    assert validate ("12.34.289.275") == False
    assert validate ("34.567.56.89") == False
    assert validate ("257.89.79.5") == False

