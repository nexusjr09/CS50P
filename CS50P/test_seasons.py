import pytest
from seasons import convert

def test_valid_dates():
    assert convert("2025-02-16") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2024-02-16") == "One million, fifty-one thousand, two hundred minutes"

def test_invalid_formats():
    with pytest.raises(SystemExit):
        convert("January 1, 1992")
    with pytest.raises(SystemExit):
        convert("1992/01/01")
    with pytest.raises(SystemExit):
        convert("01-01-1992")