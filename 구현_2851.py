arr = []
for i in range(10):
  arr.append(int(input()))

temp = []
answer = 0
a = 0
for i in range(len(arr)):
  if answer < 100:
    answer += arr[i]
  else:
    break
  a = i

temp.append(answer)
temp.append(answer-arr[a])

if abs(100 - temp[0]) > abs(100-temp[1]):
  print(temp[1])
else:
  print(temp[0])

    