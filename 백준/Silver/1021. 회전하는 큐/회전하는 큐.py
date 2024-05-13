import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
q = deque(range(1, n+1))
idx_list = list(map(int, sys.stdin.readline().split()))
cnt = 0

for x in idx_list:
    if x == q[0]:   # 뽑아내려는 원소가 첫 번째 위치했을 때
        q.popleft()
    elif q.index(x) < len(q) - q.index(x):  # 왼/오 회전 최솟값 비교
        cnt += q.index(x)
        q.rotate(-q.index(x))
        q.popleft()
    else:
        cnt += len(q) - q.index(x)
        q.rotate(len(q)-q.index(x))
        q.popleft()
print(cnt)
