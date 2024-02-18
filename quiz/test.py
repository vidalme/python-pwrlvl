import json

'''
a = ['azul','beje','caramelo']
b = []
letra=ord('A')
index=0


#c = range(ord('A'),ord('Z')+1)

for sa in a:
    b.append("( "+chr(letra)+" ) "+ sa )
    letra+=1

print(b)


with open("data.json","r") as data:

    a = json.load(data)["temas"]
    print(len(a))
    print(a[0]['name'])

    #print(a[0]['perguntas'][0]['texto'])
    #for b in a[0]['perguntas'][0]['respostas']:
    #   print(b)
    

for i in range(1,100):
    #print(chr(i))
    pass

print(type(11))
print(type("a"))    
'''
import random
a = ['banana','maca','pera']

print(a)
random.shuffle(a)
print(a)
