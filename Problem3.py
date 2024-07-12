# Write a python program to print the contents of a directory using the os module.

import os

path = '/'

entries = os.listdir(path)

for entry in entries:
    print(entry)