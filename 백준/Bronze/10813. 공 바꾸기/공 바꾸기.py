n, m = map(int, input().split())
balls = [0] * n
for i in range(n) :
    balls[i] = i+1

for _ in range(m) :
    i, j = map(int, input().split())
    temp = balls[i-1]
    balls[i-1] = balls[j-1]
    balls[j-1] = temp

print(" ".join(map(str, balls)))