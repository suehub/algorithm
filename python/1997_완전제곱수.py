m = int(input())
n = int(input())

square = []

for i in range(m, n+1) :
  for j in range(1, i+1) :
    if i % j == 0 and i // j == j :
      square.append(i)

if square :
  print(sum(square))
  print(min(square))
else :
  print(-1)