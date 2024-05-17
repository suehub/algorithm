import sys

s = sys.stdin.readline().rstrip()
stack = []

for c in s:
    if str(0) <= c <= str(9):
        stack.append(c)
    else:
        b = str(stack.pop())
        a = str(stack.pop())
        if c == '/':
            stack.append(eval(a + '//' + b))
        else:
            stack.append(eval(a + c + b))

print(stack[0])
