a = list(map(str, input()))
arr =[]
#1. 각각 1이상인 단어여야 한다.
#2. 이중 for문으로 나눌 2구간을 선택한다
#3. 뒤집은 값 다 배열에 넣고 min 값 찾기




#i=1 j=2 /i=2 j=3/ i=3 j=4/

for i in range(1, len(a)-1):
  for j in range(i+1,len(a)):
    first = a[:i]
    second = a[i:j]
    last = a[j:]
    
    first.reverse()
    second.reverse()
    last.reverse()
    arr.append("".join(first+second+last))

print(min(arr))