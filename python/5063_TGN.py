# 첫째 줄에 테스트 케이스의 개수 N이 주어진다. 
# 다음 N개의 줄에는 3개의 정수 r, e, c가 주어진다. 
# r은 광고를 하지 않았을 때 수익, e는 광고를 했을 때의 수익, c는 광고 비용이다. (-106 ≤ r,e ≤ 106, 0 ≤ c ≤ 106)

n = int(input())

for i in range(n) :
  r, e, c = map(int, input().split())
  
  if r == e - c :
    print('does not matter')
  elif r > e - c :
    print('do not advertise')
  else :
    print('advertise')
