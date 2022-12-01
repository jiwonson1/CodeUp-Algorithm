# 풀이 1 * 반례: 입력값이 _ 일때 빈칸으로 인식
a = str(input())
a = a.strip()

blank_cnt = a.count(' ')

if blank_cnt == 0:
  print(0)
else:
  print(blank_cnt+1)
  
#풀이 2
n = len(input().split())

print(n)

#split()과 split(' ')의 차이
#split()은 공백 1개이건 공백 2개이건 무조건 1개로 보고 처리
#split은 공백을 각각 처리 배열에 담을 때'' 공백도 배열에 담김