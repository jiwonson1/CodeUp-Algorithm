numbers = list(map(int, input().split()))
isQuintuple = False

for i in numbers:
    if(i % 5 == 0):
        print(i)
        isQuintuple = True
        break

if(isQuintuple == False):
    print('0')
    
