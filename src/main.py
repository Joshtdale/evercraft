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
    roll = 20
    def __init__(self, name, alignment):
        self.name = name
        self.level = 1
        self.xp = 0
        self.alignment = alignment
        self.alive = True
        self.strength = self.modifiers['10'] # modifiers[str(int('14') + int('1'))]
        self.dexterity = self.modifiers['10']
        self.armor = 10 + self.dexterity
        self.constitution = self.modifiers['10']
        self.hp = 5 + self.dexterity 
        self.wisdom = self.modifiers['10']
        self.intelligence = self.modifiers['10']
        self.charisma = self.modifiers['10']

        

    def attack(self, opponent, roll):
        hit = self.strength + self.level // 2
        if roll == 20:
            opponent.hp -= 2 + self.strength
            self.xp = self.xp + 10
        elif roll + hit >= opponent.armor:
            opponent.hp -= 1 + self.strength
            self.xp = self.xp + 10

        if opponent.hp <= 0:
            opponent.alive = False
        
        if self.xp < 1000:
            self.level = 1
        elif self.xp >= 1000:
            self.level = math.ceil(self.xp/1000)
            self.hp = 5 * self.level
        
        
        





p1 = Character('Josh', 'Evil')
p2 = Character('Dakota', 'Good')
for number in range(0, 301):
    p1.attack(p2, 20)
print (p1.roll, p1.level)





