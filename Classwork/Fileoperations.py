'''try:
    file=open('demo.txt','r')

except Exception as e:
    print(f'File is not there{e}')

else:

    content = file.read() # Reads the entire content
    file.seek(0)
    lines = file.readlines() # Reads all lines into a list
    file.seek(0)
    line = file.readline() # Reads a single line
    print(f'\nFile Content using read():\n{content}')
    print(f'\nFile Content using readlines():\n{lines}')
    print(f'\nFile Content using readline():\n{line}')
    
finally:
    print("Rest Of the code")
    file.close()
  
    
try:
    file= open('dsda.txt', 'w')
except FileNotFoundError:
    print("File Is Not Present")
else:
    file.write('Monday i wont write exam')
    file.close()
finally:
    print("Rest Of The Code")
  
    
try:
    file= open('dsda.txt', 'a+')
except FileNotFoundError:
    print("File Is Not Present")
else:
    file.write('Monday i wont write exam\n')
    file.seek(0)
    print(file.read())
    file.close()
finally:
    print("Rest Of The Code")
    
    

r- read
w-write
a-append
r+-read+write
w+-write+read
a+-append+read


with open('dsda.txt', 'r+') as file:
    file.write('\nFile operations')
    file.seek(0)
    print(file.read())

import os 

print(os.getcwd())

if not os.path.exists('DSDA'):
    os.mkdir('DSDA')


import os

if os.path.exists('DSDA'):
    os.rmdir('DSDA')


import os

if os.path.exists('DSDA'):
    os.rmdir('DSDA')
    
os.makedirs('DSDA/ 7896')
'''
import os
import shutil

if not os.path.exists('DSDA'):
    os.rmdir('DSDA')
    os.makedirs('DSDA/ 7896')
    
shutil.rmtree('DSDA')