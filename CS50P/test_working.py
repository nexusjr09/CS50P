import pytest
from working import convert


def test_full_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_no_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_mixed_times():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_midnight_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_overnight():
    assert convert("5 PM to 9 AM") == "17:00 to 09:00"


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")


def test_invalid_format():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
