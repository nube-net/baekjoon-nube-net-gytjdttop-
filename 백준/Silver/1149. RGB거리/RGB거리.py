import sys
inputF = sys.stdin.readline

n = int(inputF())
dp = [[0, 0, 0] for _ in range(n)]
house = [list(map(int, inputF().split())) for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[0][0] = house[i][0]
        dp[0][1] = house[i][1]
        dp[0][2] = house[i][2]
    else:
        dp[i][0] = house[i][0] + min(dp[i-1][1], dp[i-1][2])

        dp[i][1] = house[i][1] + min(dp[i - 1][0], dp[i - 1][2])

        dp[i][2] = house[i][2] + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[n-1]))