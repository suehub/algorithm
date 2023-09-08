n = int(input())

for _ in range(n) :
  p = int(input())

  cList = []
  nameList = []

  for _ in range(p) :
    c, name = input().split()

    cList.append(int(c))
    nameList.append(name)

  print(nameList[cList.index(max(cList))])

