t = int(input())

for _ in range(t) :
  
  sList = []
  lList = []

  n = int(input())
  
  for _ in range(n) :
    s, l = input().split()
    sList.append(s)
    lList.append(int(l))

  print(sList[lList.index(max(lList))])
