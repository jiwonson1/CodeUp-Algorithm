﻿a=input()
x=int(a)
if(x<0):
    print("minus")
    if(x%2==0):
        print("even")
    else:
        print("odd")
else:
    print("plus")
    if(x%2==0):
        print("even")
    else:
        print("odd")
