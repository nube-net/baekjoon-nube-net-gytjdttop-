import sys
input = sys.stdin.readline

dp = [[1 for _ in range(30)] for _ in range(30)]
for i in range(1,30):
    tmp = dp[i-1][i-1]
    for j in range(i,30):
        tmp += dp[i-1][j]
        dp[i][j] = tmp

for _ in range(1000):
    n = int(input())
    if n==0:
        break
    print(dp[n-1][n-1])

