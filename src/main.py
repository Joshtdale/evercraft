class Character:
    def __init__(self, name, alignment):
        modifiers = {
            '14': 2,
            '15': 3,
            '16': 4,
        }
        self.name = name
        self.alignment = alignment
        self.armor = 10
        self.hp = 5
        self.alive = True
        self.strength = modifiers['16']
        self.dexterity
        self.constitution
        self.wisdom
        self.intelligence
        self.charisma


    def attack(self, opponent, roll):
        if roll == 20:
            opponent.hp -= 2 + self.strength
        elif roll >= 10:
            opponent.hp -= 1 + self.strength
        if opponent.hp <= 0:
            opponent.alive = False


p1 = Character('Josh', 'Evil')
p2 = Character('Dakota', 'Good')
p1.attack(p2, 18)
print(p2.hp)





