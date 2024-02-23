import os
from datetime import datetime

# print(dir(os))

# print(os.getcwd())
# os.chdir('/mnt/c/Users/andri/OneDrive/Área de Trabalho')

# for i in range(1,6):
#     pass
    # os.makedirs(f'files/newfile{i}.txt')

# os.mkdir('os-demo/sub-demo')
# os.makedirs('os-demo/sub-demo')

# os.rmdir('os-demo/sub-demo')
# os.removedirs('os-demo/sub-demo')
# for i in range(1,6):
#     os.rmdir(f'files/newfile{i}.txt')

# os.rename('newfile1.txt','demo.txt')

# os.chdir('files')
# print(os.getcwd())

# mod_time = os.stat('file0.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))
# print(os.listdir())
os.chdir('/home/andre/projects/python-based-nano-projects/random/')
# print(os.walk('/'))

# print(os.listdir())

# for dirpath, dirnames, filenames in os.walk('/home/andre/projects/python-based-nano-projects/random/'):
    # print('Current path:',dirpath)
    # print('Directories:',dirnames)
    # print('Files:',filenames)
    # print()

print(os.environ.get('HOME'))