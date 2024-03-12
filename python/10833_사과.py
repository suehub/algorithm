n = int(input())
result = 0

for _ in range (n) :
  s, a = map(int, input().split())
  result += a % s

print(result)