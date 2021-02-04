a = int(input())
b = list(map(int, input().split()))
 
for i in range(a) : 
    for j in range(a) :
        print(b[j], end = ' ')
    print()
    for z in range(a-1) :
        temp = b[z]
        b[z] = b[z+1]
        b[z+1] = temp

