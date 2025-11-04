from bank import value

def test_hello_exact():
    assert value("hello") == 0

def test_hello_case_insensitive():
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_hello_phrase():
    assert value("Hello there") == 0
    assert value("  HELLO, Newman ") == 0

def test_h_exact():
    assert value("hi") == 20
    assert value("h") == 20

def test_h_case_insensitive():
    assert value("Hi") == 20
    assert value("How you doing?") == 20

def test_noh_greetings():
    assert value("test") == 100
    assert value("What's up?") == 100
    assert value("GREETINGS") == 100

def test_empty_input():
    assert value("") == 100
    assert value("    ") == 100
