a, b = map(int, input().split())
x = list(str(input()))
y = list(str(input()))

t = int(input())

x.reverse()
total = x+y

for i in range(t):
  for j in range(len(total)-1):
    if total[j] in x and total[j+1] in y:
      total[j], total[j+1] = total[j+1], total[j]

      if total[j+1] == x[-1]:
        break

print("".join(total))

#1. 타임만큼 for문을 돌리기
#2. x+y 합친 값 출력
#3. 첫번째 x의 끝값 y의 첫값 자리교체
#4. 두번째 x의 끝과 끝앞값, y의 첫갑 첫앞값 자리교체
