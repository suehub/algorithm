cnt = int(input())

for i in range(cnt) :
    a, b = map(int, input().split())
    print('Case #{0}: {1}'.format(i+1, a+b))