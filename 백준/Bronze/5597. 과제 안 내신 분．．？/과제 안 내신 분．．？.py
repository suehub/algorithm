std = []
stdNum = [0] * 30

for _ in range(28) :
    std.append(int(input()))

for x in std:
    stdNum[x-1] = 1

for i in range(len(stdNum)) :
    if stdNum[i] == 0 :
        print(i+1)
