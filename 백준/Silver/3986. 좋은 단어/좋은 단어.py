import sys

n = int(sys.stdin.readline())
cnt = n

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    stack = []

    for c in s:
        if len(stack) == 0:
            stack.append(c)
        elif c == stack[-1]:
            stack.pop()
        else:
            stack.append(c)

    if stack:
        cnt -= 1

print(cnt)