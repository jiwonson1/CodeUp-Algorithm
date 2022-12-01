#1. 배열 길이 구하기 ex 8개 
#2. 중복 줄이기 ex 3개 만나옴
#3. 중복 개수는 5개  
#4. 답은 5개     중복 개수가 정답. 
#5. 만약 6또는 9가 중복개수에 있다면 , 몫 +나머지 하면 답임. 

n = str(input())
a = []
sum = 0
for i in range(len(n)):
  if n[i] == '6' or n[i] == '9':
    sum = int(n.count('6')+n.count('9'))//2 + int(n.count('6') + n.count('9'))%2
    a.append([sum, n[i]])
  else:
    a.append([n.count(n[i]), n[i]])
  
aset = sorted(a, reverse=True)

print(aset[0][0])
