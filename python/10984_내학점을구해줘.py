t = int(input())

for i in range(t) :
  n = int(input())
  C, score = 0, 0
  
  for j in range(n) :
    c, g = input().split()
    c, g = int(c), float(g)
    C += c
    score += c * g
  
  print(C, round(score / C, 1))
