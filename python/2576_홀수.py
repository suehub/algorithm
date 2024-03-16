num, odd = [], []

for _ in range(7) :
  num.append(int(input()))

for x in num :
  if x % 2 == 1 :
    odd.append(x)

if len(odd) == 0 :
  print(-1)
else :
  print(sum(odd))
  print(min(odd))