import sys
input = sys.stdin.readline
G = int(input())
P = int(input())
parent = [i for i in range(G+1)] 
def find(curr):
    if parent[curr] == curr:
        return curr
    parent[curr] = find(parent[curr])
    return parent[curr]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

arr = [int(input()) for _ in range(P)]

ans = 0
for g in arr:
    p = find(g) 
    if p == 0:
        break
    ans += 1
    union(p-1, p)

print(ans)
