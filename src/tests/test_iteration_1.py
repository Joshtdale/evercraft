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
    assert not p1.hp > 3 and not p2.hp > 3
    assert not p1.hp < 3 and not p2.hp < 3

def test_10_or_over_attack():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    p1.attack(p2, 15)
    p2.attack(p1, 10)
    assert p1.hp == 4 and p2.hp == 4
    assert p1.hp is not 5 and p2.hp is not 5
    assert not p1.hp < 4 and not p2.hp < 4

def test_less_than_10_attack():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    p1.attack(p2, 9)
    p2.attack(p1, 3)
    assert p1.hp == 5 and p2.hp == 5
    assert not p1.hp < 5 and not p2.hp < 5

def test_alive():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    p1.attack(p2, 20)
    p1.attack(p2, 20)
    p1.attack(p2, 20)
    assert p2.alive is not True

def test_strength():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.strength == 0 and p2.strength == 0

def test_dexterity():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.dexterity == 0 and p2.dexterity == 0

def test_constitution():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.constitution == 0 and p2.constitution == 0

def test_wisdom():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.wisdom == 0 and p2.wisdom == 0

def test_intelligence():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.intelligence == 0 and p2.intelligence == 0

def test_charisma():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.charisma == 0 and p2.charisma == 0

def test_level():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.level == 1 and p2.level == 1

def test_xp():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.xp == 0 and p2.xp == 0

def test_20attack_increase_xp ():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    p1.attack(p2, 20)
    p2.attack(p1, 20)
    assert p1.xp == 10 and p2.xp == 10

def test_regular_attack_increase_xp ():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    p1.attack(p2, 12)
    p2.attack(p1, 14)
    assert p1.xp == 10 and p2.xp == 10

def test_unsuccessful_attack_xp ():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    p1.attack(p2, 8)
    p2.attack(p1, 6)
    assert p1.xp == 0 and p2.xp == 0

def test_multiple_attack_xp ():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    p1.attack(p2, 14)
    p2.attack(p1, 12)
    p1.attack(p2, 15)
    p2.attack(p1, 16)
    assert p1.xp == 20 and p2.xp == 20


def test_dexterity_mod():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.armor is 10

def test_hp_mod():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.hp is 5

def test_level_up():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    for number in range(0, 101):
        p1.attack(p2, 20)
    assert p1.level is 2

def test_multiple_level_up():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    for number in range(0, 201, 1):
        p1.attack(p2, 20)
    assert p1.level is 3

def test_hp_level_up():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    for number in range(0, 101):
        p1.attack(p2, 20)
    assert p1.hp is 10
