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
    assert p1.hp == 5 and p2.hp == 5

def test_20_attack():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    p1.attack(p2, 20)
    p2.attack(p1, 20)
    assert p2.hp == 3 and p1.hp == 3

def test_10_or_over_attack():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    p1.attack(p2, 15)
    p2.attack(p1, 10)
    assert p1.hp == 4 and p2.hp == 4

def test_less_than_10_attack():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    p1.attack(p2, 9)
    p2.attack(p1, 3)
    assert p1.hp == 5 and p2.hp == 5

def test_alive():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    p1.attack(p2, 20)
    p1.attack(p2, 20)
    p1.attack(p2, 20)
    assert p2.alive is not True

