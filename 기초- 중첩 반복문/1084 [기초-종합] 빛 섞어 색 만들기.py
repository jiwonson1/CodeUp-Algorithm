r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
count = 0
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            count += 1;
print(count);
