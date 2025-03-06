import os

os.mkdir('first')
os.mkdir('second')

with open('first/test1.txt', 'w'): ...
with open('first/test2.txt', 'w'): ...

with open('second/test1.txt', 'w'): ...
with open('second/test2.txt', 'w'): ...

for root, directories, files in sorted(os.walk('./')):
    print(root)
    for directory in sorted(directories):
        print(directory)
    for file in sorted(files):
        print(file)