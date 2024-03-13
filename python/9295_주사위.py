t = int(input())

for i in range(t) :
  num1, num2 = map(int, input().split())
  print(('Case {0}: {1}').format(i+1, num1+num2))