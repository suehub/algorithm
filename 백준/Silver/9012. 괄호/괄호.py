import sys

t = int(sys.stdin.readline())

for _ in range(t):
    s = sys.stdin.readline()
    while '()' in s:
        s = s.replace('()', '')

    if s.strip():
        print('NO')
    else:
        print('YES')