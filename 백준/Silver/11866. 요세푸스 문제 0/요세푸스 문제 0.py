import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque([x for x in range(1, n+1)])
result = []

while q:
    q.rotate(-k + 1)  # k번째 요소를 맨 앞으로 옮김
    result.append(str(q.popleft()))

print('<{}>'.format(', '.join(result)))