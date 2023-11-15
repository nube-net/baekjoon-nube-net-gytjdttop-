import sys
input = sys.stdin.readline

n = int(input())
if n%2 == 1:
    print(0)
else:
    dp = [0 for _ in range(31)]
    dp[0] = 1
    dp[2] = 3
    for i in range(4,n+1):
        if i%2 == 1:
            continue
        for j in range(0,i,2):
            if j == i-2:
                dp[i] += dp[j]*3
            else:
                dp[i] += dp[j] * 2
    print(dp[n])
