import sys
input = sys.stdin.readline

T = int(input())
for __ in range(T):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    dp = [0 for _ in range(m+1)]
    dp[0] = 1

    for c in coin:
        for i in range(c, m + 1):
            dp[i] += dp[i - c]

    print(dp[m])