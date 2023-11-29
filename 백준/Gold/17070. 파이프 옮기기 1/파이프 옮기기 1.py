import sys
input = sys.stdin.readline

n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1
ans = 0
for i in range(n):
    for j in range(2, n):
        if Map[i][j] == 0:
            if j > 0:
                dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
                dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
            if i > 0 and Map[i - 1][j] == 0 and Map[i][j - 1] == 0:
                 dp[i][j][2] = dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]

ans = sum(dp[n - 1][n - 1])
print(ans)
