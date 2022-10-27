import math
class Attack:
    def __init__(self, attacker, opponent):
        # Character.__init__(self, name, alignment)
        self.attacker = attacker
        self.opponent = opponent
    def action(self, roll):
        hit = self.attacker.attack_mod
        print(hit)
        if roll == 20:
            self.opponent.hp -= 2 + self.attacker.strength
            self.attacker.xp = self.attacker.xp + 10
        elif roll + hit >= self.opponent.armor:
            self.opponent.hp -= 1 + self.attacker.strength
            self.attacker.xp = self.attacker.xp + 10

        if self.opponent.hp <= 0:
            self.opponent.alive = False
        
        if self.attacker.xp < 1000:
            self.attacker.level = 1
        elif self.attacker.xp >= 1000:
            self.attacker.level = math.ceil(self.attacker.xp/1000)
            self.attacker.hp = 5 * self.attacker.level

class Character():
    modifiers = {
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
        16: 3,
        17: 3,
        18: 4,
        19: 4,
        20: 5,
    }
    

    def __init__(self, name, alignment):
        self.name = name
        self.level = 1
        self.xp = 0
        self.alignment = alignment
        self.alive = True
        self.strength = self.modifiers[10] # modifiers[str(int('14') + int('1'))]
        self.dexterity = self.modifiers[10]
        self.armor = 10 + self.dexterity
        self.constitution = self.modifiers[10]
        self.hp = 5 + self.dexterity 
        self.wisdom = self.modifiers[10]
        self.intelligence = self.modifiers[10]
        self.charisma = self.modifiers[10]
        self.attack_mod = self.strength + self.level // 2

        

        
        
        

class Fighter(Character):
    
    def __init__(self, name, alignment):
        Character.__init__(self,name, alignment)
        self.level = 3
        self.attack_mod = self.strength + self.level
        # Attack.__init__(name, alignment, opponent)
        # hit =  self.strength + self.level
            
        




# # p1 = Character('Josh', 'Evil')
p2 = Character('Dakota', 'Good')
c1 = Fighter('name', 'evil')
# for number in range(0, 201):
#     a = Attack(c1, p2)
#     a.action(11)
a = Attack(c1, p2)
a.action(7)

# # # c1.attack(p2, 20)# c1.attack(p2, 20)
print(c1.attack_mod, c1.level, p2.armor, p2.hp)





