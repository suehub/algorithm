import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([i for i in range(1, n+1)])

while len(q) != 1:
    q.popleft()
    q.append(q[0])
    q.popleft()

print(q[0])