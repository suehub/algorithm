import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
q = deque(range(1, n+1))

idx_list = list(map(int, sys.stdin.readline().split()))
cnt = 0

for x in idx_list:
    idx = q.index(x)
    if idx < len(q) - idx:  # 왼/오 회전 최솟값 비교
        cnt += idx
        q.rotate(-idx)
        q.popleft()
    else:
        cnt += len(q) - idx
        q.rotate(len(q)-idx)
        q.popleft()

print(cnt)