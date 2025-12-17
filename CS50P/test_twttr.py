import twttr
from twttr import shorten 

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("bigyan") == "bgyn"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("BIGYAN") == "BGYN"

def test_mixedcase():
    assert shorten("TwIttER") == "TwttR"
    assert shorten("bIgYAn") == "bgYn"

def test_numbersandsymbols():
    assert shorten("CS50!") == "CS50!"
    assert shorten("123abc#") == "123bc#"

def test_emptystrings():
    assert shorten("") == ""
    