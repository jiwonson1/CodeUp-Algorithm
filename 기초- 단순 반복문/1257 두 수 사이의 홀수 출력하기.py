startNumber, lastNumber = input().split()
startNumber = int(startNumber)
lastNumber = int(lastNumber)

for i in range(startNumber, lastNumber + 1):
    if(i % 2 == 1):
        print(i, end=' ')
