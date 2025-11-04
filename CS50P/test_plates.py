from plates import is_valid

def test_length_valid():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True

def test_length_invalid():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_start_with_two_letters_valid():
    assert is_valid("CS") == True
    assert is_valid("PZ50") == True

def test_start_with_two_letters_invalid():
    assert is_valid("1A") == False
    assert is_valid("50") == False
    assert is_valid("C5") == False
    assert is_valid("01") == False

def test_number_placement_valid():
    assert is_valid("CS50") == True
    assert is_valid("PZ07") == False

def test_number_placement_invalid():
    assert is_valid("CS50P") == False
    assert is_valid("CS50T") == False
    assert is_valid("CS50PT") == False
    assert is_valid("P3HT") == False

def test_zero_placement_invalid():
    assert is_valid("CS05") == False
    assert is_valid("AAA000") == False

def test_alphanumeric_invalid():
    assert is_valid("CS.50") == False
    assert is_valid("CS!50") == False
    assert is_valid("CS 50") == False
