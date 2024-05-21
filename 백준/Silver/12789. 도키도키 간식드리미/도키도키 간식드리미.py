import sys

input = sys.stdin.readline

n = int(input())
wait_list = list(map(int, input().split()))
stack = []
target = 1

for x in wait_list:
    while stack and stack[-1] == target:
        stack.pop()
        target += 1
    if x == target:
        target += 1
    else:
        stack.append(x)

while stack and stack[-1] == target:
    stack.pop()
    target += 1

if not stack:
    print('Nice')
else:
    print('Sad')