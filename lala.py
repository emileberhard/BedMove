import os

os.chdir('/Users/emileberhard/PycharmProjects/BedMove')

with open('readme.txt', 'a') as f:
    f.write('readme')
    f.close()