n = int(input())

for i in range(1, n+1):
    if (i == 1) or (i == n):
        for j in range(1, n+1):
            print('*', end='')
        print()
    else:
        print('*', end='')
        for j in range(1, n-1):
            print(' ', end = '')
        print('*', end ='')
        print()
    
