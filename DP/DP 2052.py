D, K = map(int, input().split(' '))

D_arr = [0 *D]

D_arr[D-1] = K


#1까지 역순
for i in range(D-1,0, -1):
    D_arr[i] = K
    