# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.
# 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.
# n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

while True :
  n = int(input())

  if n == -1 : 
    break
  
  sum = 0
  divisor = []
  
  for i in range(1, n) :
    if n % i == 0 :
      sum += i
      divisor.append(i)

  if n == sum :
    print(n, '= ', end="")

    for i in divisor :
      if i == divisor[-1] :
        print(i)
        break
      
      print(i, '+ ', end="")

  else :
    print(n, 'is NOT perfect.')
    
