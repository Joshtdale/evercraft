from main import *

def test_attack_class():
    assert Attack is not None

# -----Fighter class tests---------------------

def test_fighter_class():
    assert Fighter is not None

def test_fighter_alive():
    c1 = Fighter('Josh', 'Evil')
    c2 = Fighter('Dakota', 'Good')
    assert c1.alive == True and c2.level == True

def test_fighter_strength():
    c1 = Fighter('Josh', 'Evil')
    c2 = Fighter('Dakota', 'Good')
    assert c1.strength == 0 and c2.strength == 0

def test_fighter_dexterity():
    c1 = Fighter('Josh', 'Evil')
    c2 = Fighter('Dakota', 'Good')
    assert c1.dexterity == 0 and c2.dexterity== 0

def test_fighter_armor():
    c1 = Fighter('Josh', 'Evil')
    c2 = Fighter('Dakota', 'Good')
    assert c1.armor == 10 and c2.armor==10

def test_fighter_constitution():
    c1 = Fighter('Josh', 'Evil')
    c2 = Fighter('Dakota', 'Good')
    assert c1.constitution == 0 and c2.constitution == 0

def test_fighter_wisdom():
    c1 = Fighter('Josh', 'Evil')
    c2 = Fighter('Dakota', 'Good')
    assert c1.wisdom == 0 and c2.wisdom == 0

def test_fighter_intelligence():
    c1 = Fighter('Josh', 'Evil')
    c2 = Fighter('Dakota', 'Good')
    assert c1.intelligence == 0 and c2.intelligence == 0

def test_fighter_charisma():
    c1 = Fighter('Josh', 'Evil')
    c2 = Fighter('Dakota', 'Good')
    assert c1.charisma == 0 and c2.charisma == 0

def test_fighter_attackmod():
    c1 = Fighter('Josh', 'Evil')
    c2 = Fighter('Dakota', 'Good')
    assert c1.attack_mod == 1 and c2.attack_mod == 1

def test_fighter_hp():
    c1 = Fighter('Josh', 'Evil')
    c2 = Fighter('Dakota', 'Good')
    assert c1.hp == 10 and c2.hp == 10

def test_fighter_hp_level_2():
    c1 = Fighter('name', 'yo')
    p2 = Character('fuck', 'thisshit')
    for number in range(0, 201):
        a = Attack(c1, p2)
        a.action(20)

def test_fighter_hp_level_multiple():
    c1 = Fighter('name', 'yo')
    p2 = Character('fuck', 'thisshit')
    for number in range(0, 301):
        a = Attack(c1, p2)
        a.action(20)
    assert c1.hp == 40


# -------Rogue class tests--------------------

def test_rogue_class():
    assert Rogue is not None

def test_rogue_triple_damage():
    p1 = Rogue('Keith', 'Neutral')
    p2 = Character('some rando', 'Evil')
    a = Attack(p1, p2)
    a.action(20)
    assert p2.hp is -1

# -------Monk class tests----------------------

def test_monk_class():
    assert Monk is not None

# -------Paladin class tests--------------------

def test_paladin_class():
    assert Paladin is not None

