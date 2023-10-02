import sys
input = sys.stdin.readline

T = int(input())
for __ in range(T):
    ans = 0
    n = int(input())
    dic = {}  #  idx, cnt
    S = list(input().strip())
    for i in range(n):
        s = S[i]
        if s in dic:
            if i-dic[s][0] > 1:
                ans += dic[s][1]*((i-dic[s][0]-1)*5)
            dic[s][0] = i
            dic[s][1] += 1
        else:
            dic[s] = [i,1]
    print(ans)