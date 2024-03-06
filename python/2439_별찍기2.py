# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

n = int(input())
star = ''

for i in range(1, n+1) :
  star = ''
  for j in range(i) :
    star += '*'
  print(star.rjust(n))



# n = int(input())

# for i in range(1, n+1) :
#   for j in range(n-i) :
#     print(' ', end='')
#   for j in range(i) :
#     print('*', end='')
#   print('')
