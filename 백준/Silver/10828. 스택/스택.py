import sys

def push(x):
    stack.append(x)

def pop():
    if len(stack) > 0:
        print(stack.pop(-1))
    else:
        print(-1)

def size():
    print(len(stack))

def empty():
    if len(stack) > 0:
        print(0)
    else:
        print(1)
def top():
    if len(stack) > 0:
        print(stack[-1])
    else:
        print(-1)

stack = []
n = int(sys.stdin.readline())

for _ in range(n):
    order = sys.stdin.readline().split()
    o = order[0]
    if o == 'push':
        push(order[1])
    elif o == 'pop':
        pop()
    elif o == 'size':
        size()
    elif o == 'empty':
        empty()
    elif o == 'top':
        top()