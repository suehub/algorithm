n = int(input())
skills = list(input())
cnt = 0
l_cnt, s_cnt = 0, 0

for c in skills:
    if c == 'L':
        l_cnt += 1
    elif c == 'R':
        if l_cnt > 0 :
            cnt += 1
            l_cnt -= 1
        else:
            break
    elif c == 'S':
        s_cnt += 1
    elif c == 'K':
        if s_cnt > 0:
            cnt += 1
            s_cnt -= 1
        else:
            break
    else: # 1~9
        cnt += 1

print(cnt)