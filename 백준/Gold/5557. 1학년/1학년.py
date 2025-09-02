import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
dp = [[0 for _ in range(21)]for _ in range(n-1)]
dp[0][a[0]] = 1
for i in range(1,n-1):
    cur = a[i]
    for j in range(21):
        if cur + j < 21:
            dp[i][cur+j] += dp[i-1][j]
        if j - cur >= 0:
            dp[i][j-cur] += dp[i-1][j]
print(dp[n-2][a[n-1]])