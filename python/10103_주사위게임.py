n = int(input())

scoreA, scoreB = 100, 100

for i in range(n) :
  a, b = map(int, input().split())

  if a == b :
    continue
  elif a > b :
    scoreB -=a
  else :
    scoreA -= b


print(scoreA)
print(scoreB)