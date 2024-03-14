n, x = map(int, input().split())
numbers = input().split()
small = []

for i in numbers :
  if int(i) < x :
    small.append(i)

print(*small)