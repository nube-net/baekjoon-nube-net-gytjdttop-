import sys
n= int(input())
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    ans = 0
    tmp = 0
    cnt = 0
    cnt_1 = 0
    end = True
    for i in range(len(s)-1,-1,-1):
        # print(ans, tmp, end)
        if end:
            if s[i] == '0':
                break
            else:
                end = False
                tmp += 1
                cnt_1 = 1
                continue

        if s[i] == '1':
            if cnt >= 2:
                end = True
                ans += tmp + 1
                tmp = 0
                cnt = 0
                continue
            elif cnt == 1:
                if cnt_1 > 1:
                    break
                ans += tmp
                tmp = 1
                cnt_1 = 1
                cnt = 0
            else:
                tmp += 1
                cnt_1 += 1
        else:
            cnt += 1
            tmp += 1
    if cnt == 1 and cnt_1 == 1:
        ans +=2
    if ans == len(s):
        print('YES')
    else:
        print('NO')






