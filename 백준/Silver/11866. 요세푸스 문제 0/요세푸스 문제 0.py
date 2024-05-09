import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque([x for x in range(1, n+1)])
result = []

while len(q) > 0:   
    item = q[(k-1) % len(q)]    # 삭제할 값. q크기 < k 일 때 나머지 연산 필요
    result.append(str(item))

    for _ in range(q.index(item)):  # 제거할 원소의 이전 원소들 맨 뒤로 이동
        temp = q[0]
        q.popleft()
        q.append(temp)

    q.remove(item)

print('<{}>'.format(', '.join(result)))