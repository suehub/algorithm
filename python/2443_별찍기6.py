n = int(input())

for i in range(n, 0, -1) :
  print(' ' * (n-i) + '*' * (2*i-1))

# for i in range(1, n+1) :
#   for _ in range(i-1) :
#     print(' ', end='')
#   for _ in range(2*n - (2*i-1)) :
#     print('*', end='')
#   print()