n = int(input())
score = list(map(int, input().split()))
cnt, total_score = 0, 0

for i in range(n) :
  if score[i] == 0 :
    cnt = 0
    continue
  if score[i] == 1 :
    cnt += 1
    total_score += cnt
    
print(total_score)