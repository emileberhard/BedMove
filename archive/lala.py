import os

os.chdir('/')

with open('../readme.txt', 'a') as f:
    f.write('readme')
    f.close()