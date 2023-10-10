import sys
input = sys.stdin.readline


T = int(input())

for __ in range(T):
    n = int(input())
    end = 0
    a = [list(map(int,input().split())) for _ in range(n)]
    if n==1:
        print(min(a[0]))
        continue
    for t1, t2 in a:
        end += t1

    dp = [100001 for _ in range(end + 1)]
    dp[0] = 0
    ans =100001
    for t1, t2 in a:
        tmp = [100001 for _ in range(end + 1)]
        for i in range(end,-1,-1):
            if dp[i] != 100001:
                tmp[i] = min(tmp[i], dp[i] + t2)
                tmp[i+t1] = min(tmp[i+t1], dp[i])
        dp = list(tmp)


    for i in range(end):
        ans = min(ans, max(i, dp[i]))
    print(ans)

