N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
# coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

answer = 0
for coin in coins:
    if K >= coin:
        answer += K // coin 
        K %= coin 
        if K <= 0: 
       		break
print(answer)
