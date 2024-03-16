numbers = list(map(int, input().split()))
sum = 0

for i in numbers :
  sum += i**2

print(sum%10)