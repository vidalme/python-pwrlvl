# # asdasdasd
# s = 'eu gosto de cubo'
# l = ['bola','cubo','piramide']

# # if s.endswith( [i for i in l ] ):
# #     print('detect final de todos os itens de uma lista')

# print( [i for i in l] )

import os
import shutil

# os.chdir('files')

def create_files():
    for i in range(1,10):
        with open(f'file{i}.jpg','w') as fl:
            fl.write(f'bom dia numero{i}')

def remove_files():
    for file in os.listdir(): 
        os.remove(file)

def ignore_images(files):
    return [f for f in files if not f.endswith('.jpg')]


def backup_files():
    shutil.copytree('files','copied_files',ignore=ignore_images)

# create_files()
# remove_files()
# backup_files()
ignore_images(os.listdir('files'))
        