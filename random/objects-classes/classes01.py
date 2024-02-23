class Vida:
    def __init__(self,comeco,fim,tipo):
        self.comeco = comeco
        self.fim = fim
        self.tipo = tipo
    def inicia(self):
        print('toda vida tem inicio]')
    def termina(self):
        print('toda vida tem fim')
    def progride(self):
        print('toda vida progride até o dia que termina')

class Mamifero(Vida):
    def __init__(self,periodo_embrionario,capacidade_pulmonar, fisio):
        self.periodo_embrionario = periodo_embrionario
        self.capacidade_pulmonar = capacidade_pulmonar
        self.fisio = fisio
    def respisrar(self):
        print('todos mamiferos respiram oxigenio')
    def desenvolvimento_uterino(self):
        print('todos mamiferos passam pelo processo embrionario no utero')

class NecessidadesFisiologicas:
    def comer(self,alimento):
        print(f'Todo mamifero precisa se alimentar, esse especificamente se alimenta de {alimento}')
    def cagar(self):
        print('todo mamifero caga')
    def dormir(self):
        print('todo mamifero dorme')


m1 = Mamifero(40,'50m3',NecessidadesFisiologicas().dormir)
m2 = Mamifero(20,'150m3',NecessidadesFisiologicas().cagar)

m2.fisio()
print(m2.capacidade_pulmonar)