n = int(input())
score = list(map(float, input().split()))
max = max(score)

for i in range(n) :
  score[i] = score[i]/max*100

print(sum(score)/n)