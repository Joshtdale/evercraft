from main import *

def test_is_character():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert Character is not None

def test_is_name():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.name is not None

def test_name_unique():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.name is not p2.name

def test_alignment():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.alignment is not None and p2.alignment is not None

def test_p1_alignment_options():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.alignment == 'Good' or p1.alignment == 'Evil' or p1.alignment == 'Neutral'

def test_p2_alignment_options():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')    
    assert p2.alignment == 'Good' or p2.alignment == 'Evil' or p2.alignment == 'Neutral'

def test_character_armor():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.armor and p2.armor == 10

def test_hp():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.hp and p2.hp == 5

# def test_attack():

#     assert 