import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

stack = []

for c in s:
    if 'A' <= c <= 'Z':
        stack.append(num_list[ord(c) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        
        if c == '+':
            stack.append(a + b)
        elif c == '-':
            stack.append(a - b)
        elif c == '*':
            stack.append(a * b)
        elif c == '/':
            stack.append(a / b)

print('%.2f' % stack[0])
