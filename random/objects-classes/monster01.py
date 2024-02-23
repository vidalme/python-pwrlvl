class Monster:
    # attributes
    def __init__(self,health, energy, x_pos=0, y_pos=0):
        self.health = health
        self.energy = energy
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __len__(self): 
        return self.health

    # methods
    def attack(self,amount):
        self.energy -= 10

    def move(self,speed):
        self.x_pos += speed

monster1 = Monster(10,20, 50,25)
monster2 = Monster(energy=100,health=50)

print(monster1.health, monster2.health)
print(monster1.x_pos, monster1.y_pos)
print(monster2.x_pos, monster2.y_pos)

# print(monster.health)
# # print(f'energia do mosntro {monster.energy}')
# monster.attack(20)
# # print(f'energia do mosntro {monster.energy}')
# monster.move(5)
