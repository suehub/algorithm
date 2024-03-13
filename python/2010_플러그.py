import sys

n = int(sys.stdin.readline().rstrip())
p = 0

for _ in range(n) :
  p += int(sys.stdin.readline().rstrip())

print(p - (n-1))