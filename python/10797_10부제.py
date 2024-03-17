day = int(input())
car = list(map(int, input().split()))
result = []

for x in car :
  if x == day :
    result.append(x)

print(len(result))