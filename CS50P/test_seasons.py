import pytest
from seasons import conversion
def test_format():
        
        assert conversion("January 1 , 1992") == False
        assert conversion("01-07-2000") == False

