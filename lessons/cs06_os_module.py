"""
Python Tutorial: OS Module - Use Underlying Operating System Functionality
https://youtu.be/tJxcKyFMTGo
"""

import os
from datetime import datetime

# print(dir(os))
print(os.getcwd())

os.chdir('/Users/vivekjha/Python')

# print (os.getcwd())
print(os.listdir())

# os.mkdir('test2')
# os.makedirs('test3/subdir1')

# os.rmdir('test2')
# os.removedirs('test3/subdir1')

# print(os.listdir())

# os.rename('test', 'practice')
print(os.stat('corey_schafer'))

mod_time = os.stat('corey_schafer').st_mtime

print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, files in os.walk('/Users/vivekjha/python'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', files)
    print()

print(os.environ.get('HOME'))

# test.txt

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('/temp/test.txt'))
print(os.path.dirname('/temp/test.txt'))
print(os.path.split('/temp/test.txt'))
print(os.path.exists('/temp/test.txt'))
print(os.path.isdir('/temp/test.txt'))
print(os.path.isfile('/temp/test.txt'))
print(os.path.splitext('/temp/test.txt'))
