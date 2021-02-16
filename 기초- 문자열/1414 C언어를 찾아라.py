string = input()
string = string.upper()
c = 0
cc = 0

for i in range(0, len(string)):
    if string[i] == 'C':
        c += 1
        if i != len(string)-1 and string[i+1] == 'C':
            cc += 1

print(c)
print(cc)
