import sys
inputF = sys.stdin.readline

n, m = map(int, inputF().split())

dp = [[0]*(n+1) for _ in range(n+1)]  # 누적합
for i in range(1, n+1):
    dp[i][1:] = list(map(int, inputF().split()))

for i in range(1, n+1):   # 가로 합
    for j in range(1, n):
        dp[i][j+1] += dp[i][j]
for j in range(1, n+1):  # 세로 합
    for i in range(1, n):
        dp[i+1][j] += dp[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, inputF().split())
    print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])
