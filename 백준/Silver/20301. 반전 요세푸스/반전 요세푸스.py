import sys
from collections import deque

n, k, m = map(int, sys.stdin.readline().split())
q = deque(range(1, n+1))
cnt = 0

while q:
    if cnt//m % 2 == 0:
        for _ in range(k-1):
            q.append(q.popleft())
    else:
        for _ in range(k):
            q.appendleft(q.pop())
    cnt += 1
    print(q.popleft())