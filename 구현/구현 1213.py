#0. 짝수면 같은 문자가 2개씩 있어야함 짝수로 있어야함.
#0. 홀수면 문자 1개를 가운데 놓음
#1.뒤집어도 같으려면 a[0]과 a[n]이 같은 문자
#2. a[1] = a[n-1]
#3. a[2] = a[n-2]

name = input()
n = []

for i in name:
    n.append(i)
    
#짝수
if len(name)%2 == 0:
    flag = 1
#홀수
else:
    flag = 0
    
for i in range(len(n)):
    if n.count(n[i]) % 2 == 0:
        continue
    else:
        #개수가 짝수이면,
        if flag:
            print("I'm Sorry Hansoo")
        #개수가 홀수이면
        else:
            flag = 1
            center = n[i]

if center:
    n.remove(center)
    
    
    ##...다시...
for i in range(0, len(n), 2):
    