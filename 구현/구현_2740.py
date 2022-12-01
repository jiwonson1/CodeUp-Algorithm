N, M= map(int, input().split(' '))
arr1=[]
arr2=[]

for i in range(N):
  arr1.append(list(map(int, input().split(' '))))

M, K = map(int, input().split(' '))

for j in range(M):
  arr2.append(list(map(int, input().split(' '))))

answer = [[0]*K for _ in range(N)]

for i in range(N):
    for j in range(K):
        number = 0
        for m in range(M):
             number += arr1[i][m] * arr2[m][j]

        answer[i][j] = number

for i in answer:
    print(*i)