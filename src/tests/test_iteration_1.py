from main import *

def test_is_character ():
    # p1 = Character('Josh')
    assert Character is not None

def test_is_name ():
    # p1 = Character('Josh')
    assert p1.name is not None

def test_name_unique ():
    assert p1.name is not p2.name

def test_alignment ():
    assert p1.alignment is not None and p2.alignment is not None

def test_p1_alignment_options ():
    assert p1.alignment == 'Good' or p1.alignment == 'Evil' or p1.alignment == 'Neutral'

def test_p2_alignment_options ():
    assert p2.alignment == 'Good' or p2.alignment == 'Evil' or p2.alignment == 'Neutral'

    