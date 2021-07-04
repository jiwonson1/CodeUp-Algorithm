string = input()
count = 0

for i in range(0, len(string)-4):
    if string[i:i+4] == 'love':
        count += 1
        
print(count)
