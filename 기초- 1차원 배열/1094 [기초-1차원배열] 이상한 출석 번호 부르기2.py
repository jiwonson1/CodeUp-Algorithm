n = int(input())
a = input().split()

numbers = []

for i in range(0, n):
  numbers.append(int(a[i]))

for i in reversed(range(n)):
  print(numbers[i], end=' ');

