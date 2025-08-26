import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n):
    dp[i + 1] = max(dp[i + 1], dp[i])

    end = i + a[i][0]
    if end <= n:
        dp[end] = max(dp[end], dp[i] + a[i][1])

print(max(dp))
