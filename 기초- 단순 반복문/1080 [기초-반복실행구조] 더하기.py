﻿a = int(input())
c = 0
for i in range(1, a+1):
    c+=i
    if c>=a:
        print(i)
        break
