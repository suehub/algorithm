v = int(input())
votes = list(input())

result = 0

for i in votes :
  if i == 'A' :
    result += 1
  else :
    result -= 1

if result == 0 :
  print('Tie')
elif result > 0 :
  print('A')
else :
  print('B')