for i in range(5):
    for j in range(5):
        print(' @', end=' ')
    print()
    
for i in range(5):
    for j in range(5):
        print(i, end=' ')
    print()
    
    
for i in range(5):
    for j in range(5):
        print(j, end=' ')
    print()
    
    
for i in range(5):
    for j in range(i+1):
        print('😀', end=' ')
    print()
    
    
for i in range(5):
    for j in range(5-i):
        print('😀', end=' ')
    print()
    
    
for i in range(5):
    for j in range(5-i):
        print(' ', end=' ')
    for j in range(i):
        print('*', end=' ')
    print()


for i in range(5):
    for spc in range(i):
        print('  ',end='')
    for j in range(5-i):
        print("😀",end='')
    print()
    

for i in range(10):
    if i<=10//2:
        print(' 😀'*(i+1),end='')
    else:
        print(' 😀'*(10-i),end='')
    print()
    


for i in range(5):
    for j in range(5):
        if i == 0 or i == 5 - 1 or j == 0 or j == 5 - 1:
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()


for i in range(5):
    for j in range(5):
        if i == 0 or i == 5 - 1 or j == 0 or j == 5 - 1 or i==5//2 or j==5//2:
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()


for i in range(5):
    for j in range(5):
        if i == 0 or i == 5 - 1 or i+j==5-1:
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()


for i in range(5):
    for j in range(5):
        if i==j or i+j==5-1:
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()