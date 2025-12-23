import pytest
from um import count

def test_counting():
    assert count("Hello,um warhap um") == 2
    assert count("um,really") == 1
    assert count("um,bro i know um um um ") == 4

def test_invalidcounts():
    assert count("Yumm,ok bro") == None
    assert count("ummm,ok bummbumm") == None

def test_case_sensitivity():
    assert count("Um, thanks for the album.") == 1
    assert count("UM, checking, um...") == 2