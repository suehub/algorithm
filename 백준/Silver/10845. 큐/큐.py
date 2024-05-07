import sys

n = int(sys.stdin.readline())
queue = []

def push(queue, x) :
    queue.append(x)

def pop(queue) :
    if len(queue) > 0 :
        print(queue[0])
        queue.__delitem__(0)
    else:
        print(-1)

def size(queue) :
    print(len(queue))

def empty(queue) :
    if len(queue) > 0 :
        print(0)
    else :
        print(1)

def front(queue) :
    if len(queue) > 0:
        print(queue[0])
    else :
        print(-1)

def back(queue) :
    if len(queue) > 0:
        print(queue[-1])
    else :
        print(-1)


for _ in range(n) :
    order = sys.stdin.readline().split()
    if 'push' in order:
        push(queue, order[1])
    elif order[0] == 'pop':
        pop(queue)
    elif order[0] == 'size':
        size(queue)
    elif order[0] == 'empty':
        empty(queue)
    elif order[0] == 'front':
        front(queue)
    elif order[0] == 'back':
        back(queue)
