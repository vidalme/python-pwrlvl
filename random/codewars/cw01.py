# ('Buy a !car [!red green !white] [cheap or !new]')  =>  ['Buy', 'a', '!car', '[!red green !white]', '[cheap or !new]']
# ('!Learning !javascript is [a joy]')                =>  ['!Learning', '!javascript', 'is', '[a joy]']
# ('[Cats and dogs] are !beautiful and [cute]')       =>  ['[Cats and dogs]', 'are', '!beautiful', 'and', '[cute]']
# '[srdutzjucj', 'Upoiqgzoyk', '!hgiesxqfh']         =>  ['srdutzjucj', 'Upoiqgzoyk', '!hgiesxqfh']

s1 = ('Buy a !car [!red green !white] [cheap or !new]')
s2 = ('!Learning !javascript is [a joy]')
s3 = ('[Cats and dogs] are !beautiful and [cute]')
s4 = ('[andre] [vidal [almeida')
s5 = ('Qbaaouhhuq Dgxvtbznpe [Ohykzfdrch !Sqypyqwgz] !fwttvdmxe [Vkdzepamsy] [!zhybrawyi Svazxcppkk Rkpllhciin] [Gowkgpaisy] [Ukvqkufrtx sforchpnxx !Bbnbwasiy')
s7 = ('['']')

def clever_split(s):
    if s == '['']':
        return []
    lista = s.split(" ")
    nova_lista=[]
    i = 0
    t = 0
    for word in lista:
        nova_word = word
        if word.startswith('['):
            nova_word = word.replace('[','')
            t=i
        if word.endswith(']'):
            temp_lista = []
            for j in range(t,i):nova_lista.pop(-1)
            for j in range(t,i+1):temp_lista.append(lista[j])
            nova_word = " ".join(temp_lista)
        nova_lista.append(nova_word)
        i+=1
    return nova_lista
    

print(clever_split(s7))