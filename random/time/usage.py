import time

#pega o epoch e torna legivel
print(time.ctime(0))


#quanto tempo desde o epoch
print(time.time())

# combinando os dois
print(time.ctime(time.time()))


# criando o objeto time
time_object = time.localtime()
print(time.strftime("%x",time_object))
print(time.strftime("%X",time_object))
print(time.strftime("%y%m%d%H%M%S",time_object))
print(time.strftime("%y%m%d",time_object))