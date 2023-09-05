while True :
  m, f = map(int, input().split())

  if m == 0 and f == 0 :
    break

  if 1 > m or f > 5 :
    continue
  
  print(m + f)