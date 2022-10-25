from main import *

def test_is_character ():
    p1 = Character('Josh')
    assert Character is not None

def test_is_name ():
    p1 = Character('Josh')
    assert p1.name is not None
