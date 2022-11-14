n = int(input())
temp = ""
arr =[]
answer = []
for i in range(n):
  arr.append(str(input()))

for i in range(n):
  t = len(arr[i])
  sum = 0
  a =0
  for j in range(t):
    if arr[i][j] == 'O':
      a+=1
      sum+=a
      if j == t-1:
        answer.append(sum)
    else:
      a=0
      if j == t-1:
        answer.append(sum)

for i in range(n):
    print(answer[i])