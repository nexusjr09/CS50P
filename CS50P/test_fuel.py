import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/1") == 100
    assert convert("0/100") == 0
    assert convert("2/3") == 67
    assert convert("1/3") == 33

    for x in ["3/2", "a/b", "1/one", "1.5/3", "-1/2", "1:-2", "1:2"]:
        with pytest.raises(ValueError):
            convert(x)

    for x in ["1/0", "100/0"]:
        with pytest.raises(ZeroDivisionError):
            convert(x)

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
