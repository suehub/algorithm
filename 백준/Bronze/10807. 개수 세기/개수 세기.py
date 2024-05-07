n = int(input())
numbers = list(map(int, input().split()))
findNum = int(input())
cnt = 0

for i in numbers :
    if i == findNum :
        cnt += 1

print(cnt)