import sys

n = int(sys.stdin.readline())
cnt = n

for _ in range(n):
    word = sys.stdin.readline()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:-1]:
            cnt -= 1
            break

print(cnt)