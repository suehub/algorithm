m = int(input())
n = int(input())
result = []

for i in range(m, n+1) :
  for j in range(2, i+1) :
    if i % j == 0 :
      if i == j :
        result.append(j)
      else :
        break

if len(result) == 0 :
  print(-1)
else :
  print(sum(result))
  print(min(result))
