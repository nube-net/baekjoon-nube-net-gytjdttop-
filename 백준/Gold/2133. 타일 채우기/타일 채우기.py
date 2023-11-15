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
        dp[i] = dp[i-2]*4-dp[i-4]
    print(dp[n])
