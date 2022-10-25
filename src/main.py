class Character:
    def __init__(self, name, alignment):
        align = ['Good', 'Evil', 'Neutral']
        self.name = name
        self.alignment = alignment






p1 = Character('Josh', 'Evil')
p2 = Character('Dakota', 'Good')
print(p1.name, p2.name)