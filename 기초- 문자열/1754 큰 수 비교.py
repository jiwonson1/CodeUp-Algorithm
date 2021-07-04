inStr = input().split()

if len(inStr[0]) < len(inStr[1]):
    print(inStr[0] + ' ' + inStr[1])
elif len(inStr[0]) > len(inStr[1]):
    print(inStr[1] + ' ' + inStr[0])
else:
    for i in range(len(inStr[0])):
        if inStr[0][i] < inStr[1][i]:
            print(inStr[0] + ' ' + inStr[1])
            break
        elif inStr[0][i] > inStr[1][i]:
            print(inStr[1] + ' ' + inStr[0])
            break
        else:
            continue
