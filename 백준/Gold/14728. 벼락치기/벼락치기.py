import sys
inputF = sys.stdin.readline

n, k = map(int, inputF().split())

dp = [0]*(k+1)

for _ in range(n):
    x, y = map(int, inputF().split())

    for i in range(k, -1, -1):
        if x <= i:
            dp[i] = max(dp[i], dp[i-x] + y)

print(dp[k])
