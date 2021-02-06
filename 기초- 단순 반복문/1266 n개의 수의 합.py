n = int(input())
numbers = list(map(int, input().split()))
sum = 0

for number in numbers:
    sum += number
print(sum)
