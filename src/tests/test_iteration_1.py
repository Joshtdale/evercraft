from main import *
#TEST FOR INITIAL CHARACTER CLASS

#Testing if there is a Character Class
def test_is_character():   
    p1 = Character('Josh', 'Evil')     
    p2 = Character('Dakota', 'Good')
    assert Character is not None

#Testing if there is a name attribute in character class
def test_is_name():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')    
    assert p1.name is not None and p2.name is not None

#Testing if there is an xp attribute
def test_is_xp():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')    
    assert p1.xp == 0 and p2.xp == 0

#Testing if there is a level attribute
def test_is_level():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')    
    assert p1.level == 1 and p2.level == 1

#Testing if there is an alive attribute set to true
def test_is_alive():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.alive == True and p2.level == True

#Testing if there is a strength attribute
def test_is_strength():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.strength == 0 and p2.strength == 0

#Testing if there is a dexterity attribute
def test_is_dexterity():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.dexterity == 0 and p2.dexterity== 0

#Testing if there is an armor attribute
def test_is_armor():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.armor == 10 and p2.armor==10

#Testing if there is a constitution attribute
def test_is_constitution():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.constitution == 0 and p2.constitution == 0

#Testing if there is a wisdom attribute
def test_is_wisdom():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.wisdom == 0 and p2.wisdom == 0

#Testing if there is an intelligence attribute
def test_is_intelligence():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.intelligence == 0 and p2.intelligence == 0

#Testing if there is a charisma attribute
def test_is_charisma():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.charisma == 0 and p2.charisma == 0 

def test_is_attackmod():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.attack_mod == 0 and p2.attack_mod==0

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
    assert p2.alignment == 'Good' or p2.alignment == 'Evil' or p2.alignment == 'Neutral' and p1.alignment == 'Good' or p1.alignment == 'Evil' or p1.alignment == 'Neutral'

def test_character_armor():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.armor and p2.armor == 10

def test_hp():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.hp == 5 and p2.hp == 5

#Test if character alive boolean changes to false when hp < 0
def test_alive():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    a = Attack(p1, p2)
    a.action(20)
    a.action(20)
    a.action(20)
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

# ----Character modifier test-----------------------

def test_dexterity_mod():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.armor is 10

def test_hp_mod():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    assert p1.hp is 5

#Testing if attack mod increases at level 2
def test_attack_mod():
    p1 = Character('name', 'Neutral')
    p2 = Character('fuck', 'thisshit')
    for number in range(0, 101):
        a = Attack(p1, p2)
        a.action(20)
    assert p1.level == 2 and p1.attack_mod == 1

#Testing if attack mod doesnt increase on level 3
def test_attack_mod_odd():
    p1 = Character('name', 'Neutral')
    p2 = Character('fuck', 'thisshit')
    for number in range(0, 201):
        a = Attack(p1, p2)
        a.action(20)
    assert p1.level == 3 and p1.attack_mod == 1

#Testing if character attack mod increases on even level
def test_attack_mod_odd():
    p1 = Character('name', 'Neutral')
    p2 = Character('fuck', 'thisshit')
    for number in range(0, 301):
        a = Attack(p1, p2)
        a.action(20)
    assert p1.level == 4 and p1.attack_mod == 2

#---------REGULAR CHARACTER CLASS ATTACK TESTS------------------------------------------------------------

#Testing if character takes damage on crit
def test_20_attack():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    a = Attack(p1, p2).action(20)
    a2 = Attack(p2, p1).action(20)
    assert p2.hp == 3 and p1.hp == 3
    assert not p1.hp > 3 and not p2.hp > 3
    assert not p1.hp < 3 and not p2.hp < 3

#Checking if character does damage on successful attacks
def test_10_or_over_attack():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    a = Attack(p1, p2).action(15)
    a2 = Attack(p2, p1).action(10)
    assert p1.hp == 4 and p2.hp == 4
    assert p1.hp is not 5 and p2.hp is not 5
    assert not p1.hp < 4 and not p2.hp < 4

#Making sure character does not do damage on unsuccessful attacks
def test_less_than_10_attack():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    a = Attack(p1, p2).action(9)
    a2 = Attack(p1, p2).action(3)
    assert p1.hp == 5 and p2.hp == 5
    assert not p1.hp < 5 and not p2.hp < 5


# ------Attack xp tests------------------

#Testing for xp increases on successful attacks
def test_20attack_increase_xp ():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    a = Attack(p1, p2).action(20)
    a2 = Attack(p2, p1).action(20)
    assert p1.xp == 10 and p2.xp == 10

#Testing for xp increases on successful attacks
def test_regular_attack_increase_xp ():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    a = Attack(p1, p2)
    a2 = Attack(p2, p1)
    a.action(12)
    a2.action(14)
    assert p1.xp == 10 and p2.xp == 10

#Making sure xp doesn't increase on unsuccessful attacks
def test_unsuccessful_attack_xp ():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    a = Attack(p1, p2)
    a2 = Attack(p2, p1)
    a.action(8)
    a2.action(6)
    assert p1.xp == 0 and p2.xp == 0

#Testing if xp levels up on multiple successful attacks
def test_multiple_attack_xp ():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    a = Attack(p1, p2)
    a2 = Attack(p2, p1)
    a.action(14)
    a.action(15)
    a2.action(12)
    a2.action(16)
    assert p1.xp == 20 and p2.xp == 20

# -----Level up tests------------------------------

#Checking if character levels up after xp is reached
def test_level_up():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    for number in range(0, 101):
        a = Attack(p1, p2)
        a.action(20)
    assert p1.level is 2

#Checking if character levels up multiple times after xp is reached
def test_multiple_level_up():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    for number in range(0, 201, 1):
        a = Attack(p1, p2)
        a.action(20)
    assert p1.level is 3

#Testing if hp is leveling up
def test_hp_level_up():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    for number in range(0, 101):
        a = Attack(p1, p2)
        a.action(20)
    assert p1.hp is 10

#Testing if hp is leveling up multiple times
def test_multiple_hp_level_up():
    p1 = Character('Josh', 'Evil')
    p2 = Character('Dakota', 'Good')
    for number in range(0, 201):
        a = Attack(p1, p2)
        a.action(20)
    assert p1.hp is 15


