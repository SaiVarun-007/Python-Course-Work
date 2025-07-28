for i in range(5):
    for j in range(5):
        if i == 0 or i == 5-1 or j ==5//2:
            print('*',end='')
        else:
            print(' ',end ='')
    print()

for i in range(5):
    for j in range(5):
        if j == 0 or j == 5-1 or i ==5//2:
            print('*',end='')
        else:
            print(' ',end ='')
    print()


for i in range(9):
    for j in range(9):
        if (j==0 or j==9-1) and i<=9//2 or (i-j==9//2 and i>=9//2) and j<=9//2 or (j-i==9//2 and j>=9//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    

