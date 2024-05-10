import sys

alpha = [chr(x) for x in range(ord('a'), ord('z')+1)]
result = [-1 for _ in range(26)]

s = sys.stdin.readline().rstrip()

for c in s:
    if c in alpha:
        result[alpha.index(c)] = s.index(c)

print(' '.join(map(str, result)))