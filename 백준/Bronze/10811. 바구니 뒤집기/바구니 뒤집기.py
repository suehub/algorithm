import sys

n, m = map(int, sys.stdin.readline().split())
numbers = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    temp = numbers[i-1:j][::-1]
    numbers[i-1:j] = temp

result = ' '.join(map(str, numbers))

print(result)