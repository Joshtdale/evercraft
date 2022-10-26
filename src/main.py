import math
class Character:
    modifiers = {
        '1': -5,
        '2': -4,
        '3': -4,
        '4': -3,
        '5': -3,
        '6': -2,
        '7': -2,
        '8': -1,
        '9': -1,
        '10': 0,
        '11': 0,
        '12': 1,
        '13': 1,
        '14': 2,
        '15': 2,
        '16': 3,
        '17': 3,
        '18': 4,
        '19': 4,
        '20': 5,
    }
    def __init__(self, name, alignment):
        self.name = name
        self.level = 1
        self.xp = 0
        self.alignment = alignment
        self.armor = 10
        self.hp = 5
        self.alive = True
        self.strength = self.modifiers['10'] # modifiers[str(int('14') + int('1'))]
        self.dexterity = self.modifiers['10']
        self.constitution = self.modifiers['10']
        self.wisdom = self.modifiers['10']
        self.intelligence = self.modifiers['10']
        self.charisma = self.modifiers['10']
        if self.xp < 1000:
            self.level = 1
        elif self.xp > 1000:
            self.level = math.ceil(self.xp/1000)

    def attack(self, opponent, roll):
        if roll == 20:
            opponent.hp -= 2 + self.strength
        elif roll >= opponent.armor:
            opponent.hp -= 1 + self.strength
        if opponent.hp <= 0:
            opponent.alive = False



p1 = Character('Josh', 'Evil')
p2 = Character('Dakota', 'Good')

print (p1.level)





