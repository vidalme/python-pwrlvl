class Monster:
    def __init__(self,hp):
        self.hp = hp
    def get_dmg(self,amount):
        self.hp -= amount

class Hero:
    def __init__(self,strength):
        self.strength = strength
    
    def attack(self,monster):
        monster.get_dmg(self.strength)

m = Monster(100)
h = Hero(10)

print(m.hp)
h.attack(m)
print(m.hp)