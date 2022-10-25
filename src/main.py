class Character:
    def __init__(self, name, alignment):
        self.name = name
        self.alignment = alignment
        self.armor = 10
        self.hp = 5
    
    def attack(self, opponent, roll):
        
        if roll == 20:
            opponent.hp -= 2
        elif roll >= 10:
            opponent.hp -= 1


p1 = Character('Josh', 'Evil')
p2 = Character('Dakota', 'Good')
p1.attack(p2, 15)
p2.attack(p1, 10)
print(p1.hp)





