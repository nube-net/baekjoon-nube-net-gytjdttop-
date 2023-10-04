import sys
inputF = sys.stdin.readline

n = int(inputF())
house = [list(map(int, inputF().split())) for _ in range(n)]

ans = float('inf')
for st in range(3):
    dp = [[float('inf'), float('inf'), float('inf')] for _ in range(n)]
    dp[0][st] = house[0][st]
    for i in range(1,n):
        dp[i][0] = house[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = house[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = house[i][2] + min(dp[i - 1][0], dp[i - 1][1])
    dp[n-1][st] = float('inf')
    ans = min(ans, min(dp[n-1]))
print(ans)
