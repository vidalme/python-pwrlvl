class Monster:
    def __init__(self,func):
        self.action = func

class Attacks:
    def bite(self):
        print('monster bit')
    def strike(self):
        print('monster stroke')
    def slash(self):
        print('monster slashed')
    def kick(self):
        print('monster kicked')

mm = Monster(func = Attacks().bite)
mm.action()

