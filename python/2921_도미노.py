n = int(input())
score = 0

for i in range(n+1) :
  for j in range(i+1) :
    score += i + j

print(score)
