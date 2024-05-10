import sys
from collections import deque

result = []
cnt = 0
n, k, m = map(int, sys.stdin.readline().split())
q = deque([i for i in range(1, n+1)])

while q:
    if cnt != 0 and cnt % m == 0:
        q.reverse()
    q.rotate(-k+1)
    result.append(q.popleft())
    cnt += 1

for x in result:
    print(x)