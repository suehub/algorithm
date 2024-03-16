n = int(input())
numbers = input().split()
result = []

for x in numbers :
  x = int(x)
  for i in range(2, x+1) :
    if x % i == 0 :
      if x == i :
        result.append(x)
      else :
        break

print(len(result))

# for x in numbers :
#   x = int(x)
#   list = []
#   for i in range(2, x+1) :
#     if x % i == 0 :
#       list.append(i)
#   if len(list) == 1 :
#     result.append(x)

# print(len(result))