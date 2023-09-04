import sys
import copy
T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
coins = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0]*(T+1)
dp[0] = 1
for coin, k in coins:
    for i in range(T,0,-1): # 큰 금액부터 탐색
        if i-coin < 0:
            break
        for j in range(coin, coin*k+1, coin):
            if i-j < 0:
                break
            dp[i] += dp[i-j]
print(dp[-1])

