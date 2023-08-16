# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

i = 0
sum = 0

s = int(input())

for i in range(1, s+2) :
    if sum >= s :
        i -= 1
        n = i
        sum -= n
        if s - sum <= i - 1 :
            n -= 1
        break
    else :
        n = i
        sum += i

print(n)



######## 더 간결한 코드 #########

# i = 0
# sum = 0

#s = int(input())

# while sum + i < s :
#     i += 1
#     sum += i

# print(i)