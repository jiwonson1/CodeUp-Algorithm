d,k = map(int,input().split())

dp = [0 for i in range(d)]
dp[0],dp[1] = 1,1

while(True):
    for i in range(2,d):
        dp[i] = dp[i-1]+dp[i-2]
    
    if dp[d-1] == k:
        print(dp[0],dp[1],sep="\n")
        break
    # a-b 차가 큰거라서 a의 값을 +해줌, b는 a값으로 세팅 
    elif dp[-1] > k:
        dp[0] += 1
        dp[1] = dp[0]
    #a-b 폭이 작은것, 따라서 b값을 키워줌
    else:
        dp[1] += 1
        
        
        #9 2 11 13 24 (7)/ 9 5 14 19 33(4)