# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# n = int(input())
# a, b = 0, 1

# for i in range(n-1) :
#   if n == 2 :
#     b = 1
#     break
#   a, b = b, a + b

# print(b)


n=int(input())

fibo = [0, 1]

for i in range(1, n) :
  fibo.append(fibo[i] + fibo[i-1])

print(fibo[n])
