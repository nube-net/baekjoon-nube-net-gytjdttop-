import sys
input = sys.stdin.readline

t = int(input())
k = 0
coins = [1, 10, 25]

for _ in range(t):
    dp = [(10 ** 15) + 1]*100
    dp[0] = 0
    ans = 0

    cost = int(input())
    for i in coins:
        for j in range(i, 100):
            dp[j] = min(dp[j], dp[j-i]+1)

    while cost > 0:
        ans += dp[cost%100]
        cost //= 100

    print(ans)