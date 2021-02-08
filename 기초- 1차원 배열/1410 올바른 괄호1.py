string = input()
open = 0
close = 0

for i in range(0, len(string)):
    if string[i] == '(':
        open += 1
    elif string[i] == ')' :
        close += 1
print(open, close)

