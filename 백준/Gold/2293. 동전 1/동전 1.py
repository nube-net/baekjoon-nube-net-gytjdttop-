import sys
inputF = sys.stdin.readline

n, k = map(int, inputF().split())
coins =[int(inputF()) for _ in range(n)]

dp = [0]*(k+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = dp[i] + dp[i-coin]

print(dp[k])
