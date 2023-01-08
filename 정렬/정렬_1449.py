a, b = map(int, input().split())
arr = list(map(int, input().split()))

start = arr[0]
end = arr[0]+b

cnt = 1

for i in range(a):
    if start <= arr[i] < end:
        continue
    else:
        start =arr[i]
        end = arr[i] + b
        cnt += 1
print(cnt)