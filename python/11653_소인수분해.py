# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

n = int(input())

i = 2
result = []

while True :
    if n == 1 : 
        break
 
    if n % i == 0 :
        result.append(i)
        n //= i
        i -= 1
    
    i += 1

result.sort()

for i in result :
   print(i)
    