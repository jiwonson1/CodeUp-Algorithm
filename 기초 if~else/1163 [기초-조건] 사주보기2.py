x,y,z=map(int,input().split())

n =(x+y+z)%1000
n = int(n/100)

if(n%2) ==0:
    print('대박')
else:
    print('그럭저럭')
