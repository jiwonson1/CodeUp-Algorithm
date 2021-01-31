startAlphabet, finalAlphabet = input().split()
startAlphabet = ord(startAlphabet)
finalAlphabet = ord(finalAlphabet)

for i in range(startAlphabet, finalAlphabet + 1):
    print(chr(i), end=' ')

