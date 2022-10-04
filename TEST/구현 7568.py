n = int(input())
arr = [] # [[55,185], [58,183]]
answer = []

for i in range(n):
  k, h = map(int, input().split(' '))
  arr.append([k,h])


# 순위 분석
for i in range(n):
  count = 0
  for j in range(n):
    if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
      count +=1
  answer.append(count+1)

# 정답 출력
for k in answer:
  print(k, end=' ')