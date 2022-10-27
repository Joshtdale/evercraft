import math

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
    
    align = {
        'Good': 'Good',
        'Neutral': 'Neutral',
        'Evil': 'Evil'
    }
    

    def __init__(self, name, alignment):
        self.classname = ''
        self.name = name
        self.level = 1
        self.xp = 0
        self.alignment = alignment
        self.alive = True
        self.strength = self.modifiers[10] # modifiers[str(int('14') + int('1'))]
        self.dexterity = self.modifiers[10]
        self.constitution = self.modifiers[10]
        self.hp_mod = 5
        self.hp = self.level * self.hp_mod
        self.wisdom = self.modifiers[10]
        self.armor = 10 + self.dexterity
        self.intelligence = self.modifiers[10]
        self.charisma = self.modifiers[10]
        self.attack_mod = self.strength + self.level // 2
        self.crit_mod = 1
        self.damage = 1
        

class Attack:
    def __init__(self, attacker, opponent):
        if attacker.classname == "Rogue":
            opponent.armor = opponent.armor - opponent.dexterity
            
        self.attacker = attacker
        self.opponent = opponent
    def action(self, roll):
        hit = self.attacker.attack_mod
        print('that boy hit', hit)
        if roll == 20:
            self.opponent.hp -= (2 + self.attacker.strength) * self.attacker.crit_mod
            self.attacker.xp = self.attacker.xp + 10
            
        elif roll + hit >= self.opponent.armor:
            self.opponent.hp -= self.attacker.damage + self.attacker.strength
            self.attacker.xp = self.attacker.xp + 10
    
        if self.opponent.hp <= 0:
            self.opponent.alive = False
        
        if self.attacker.xp < 1000:
            self.attacker.level = 1
        elif self.attacker.xp >= 1000:
            self.updateAttr()
        
    def updateAttr(self):
            self.attacker.level = math.ceil(self.attacker.xp/1000)
            self.attacker.hp  = self.attacker.level * self.attacker.hp_mod
            self.attacker.attack_mod = self.attacker.strength + self.attacker.level // 2


        

class Fighter(Character):
    
    def __init__(self, name, alignment):
        Character.__init__(self,name, alignment)
        self.attack_mod = self.strength + self.level
        self.hp_mod = 10
        self.hp = 10

            
        

class Rogue(Character):
    
    def __init__(self, name, alignment):
        align = {
            'Neutral': 'Neutral',
            'Evil': 'Evil'
            }
        Character.__init__(self, name, alignment)
        self.classname = 'Rogue'
        self.alignment = align[alignment]
        self.crit_mod = 3
        self.attack_mod = self.dexterity + self.level // 2
        self.hp_mod = 10
        self.hp = 10

class Monk(Character):
    def __init__(self, name, alignment):
        align = {
            'Good': 'Good',
            'Neutral': 'Neutral',
            'Evil': 'Evil'
            }
        Character.__init__(self, name, alignment)
        self.classname = 'Monk'
        self.hp_mod = 6
        self.hp = 6
        self.damage = 3
        self.armor = self.armor + (self.dexterity + self.wisdom)
    
    def updateAC(self):
        self.armor = self.armor + (self.dexterity + self.wisdom)

class Paladin(Character):
    pass


# p1 = Character('name', 'Neutral')
# p2 = Character('fuck', 'thisshit')
# # for number in range(0, 101):
# a = Attack(p1, p2)
# a.action(20)
# # # a.action(9)
# # print (p1.level, p1.attack_mod, p2.hp)
# # print(c1.level, c1.hp)
# print(p2.armor)
p1 = Monk('Keith', 'Neutral')
p1.wisdom = p1.modifiers[12]
print(p1.wisdom, p1.armor)






