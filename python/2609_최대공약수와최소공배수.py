# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.


a, b = map(int, input().split())

def gcd(a, b) :
  while b != 0 :
    a, b = b, a % b
  return a

gcd = gcd(a, b)
lcm = a * b // gcd

print(gcd, lcm, sep='\n')

# a, b = map(int, input().split())
# q, r, gcd = 1, 1, 1

# q = min(a, b)
# r = max(a, b) % q

# if r == 0 :
#   gcd = q
# else :
#   while r != 0 :
#     q, r = r, q % r
#   gcd = q

# lcm = a * b // gcd

# print(gcd, lcm, sep='\n')