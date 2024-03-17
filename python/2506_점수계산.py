n = int(input())
score = list(map(int, input()))
total_score = 0

for i in len(score) :
  if score[i] == 1 :
    total_score += 1
    if i > 0 and score[i-1] == 1 :
      total_score += 1