n = int(input())
a, b = 0, 1

def f(a, b) :
  return a + b

for _ in range(1, n):
  a, b = b, f(a, b)
  
print(b)