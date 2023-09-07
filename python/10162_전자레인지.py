# 버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초
# 제시된 3개의 버튼으로 T초를 맞출 수 없으면 음수 -1을 출력

t = int(input())

a = 60 * 5
b = 60
c = 10

tA = t // a 
tB = (t % a) // b
tC = (t % b) // c

if t  == tA*a + tB*b + tC*c :
  print(tA, tB, tC)
else :
  print(-1)