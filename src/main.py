class Character:
    def __init__(self, name, alignment):
        self.name = name
        self.alignment = alignment
        self.armor = 10
        self.hp = 5
    
    def attack(attacker, opponent, roll):
        
        if roll == 20:
            opponent.hp -= 2
        elif roll >= 10:
            oponent.hp -= 1

p1 = Character('Josh', 'Evil')
p2 = Character('Dakota', 'Good')
Character.attack(p1, p2, 20)
print(p2.hp)





