a,r,n = input().split()

A = int(a)
R = int(r)
N = int(n)

for i in range(N-1):
    A = A*R

print(A)
    
