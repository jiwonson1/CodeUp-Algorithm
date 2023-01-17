N, L = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort()

cnt = 0

for pool in range(len(lst)):
    #물웅덩이 길이
    length = lst[pool][1] - list[pool][0]
    #마지막 웅덩이일 경우
    if pool == len(lst)-1 :
        #index를 맞추기 위해 -1을 추가로 해주고 나눈 값을 더해준다.
        cnt += (length-1) // L +1
        break
    
    if (length)%L :
        tmp = L - ((length)%L)
        now_corver = lst[pool][1] + tmp
        
        if lst[pool+1][0] <= now_corver:
            lst[pool+1][0] = now_corver
        cnt+= (length)//L +1
    else :
        cnt += (length) //L