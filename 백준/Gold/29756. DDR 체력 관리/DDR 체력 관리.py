import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[-1 for _ in range(101)] for _ in range(n)]

s = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))

dp[0][100]= 0
idx= 100-h[0]+k
if idx >100:
    idx = 100
dp[0][idx] = s[0]

for i in range(1,n):
    for j in range(101):  # 체력
        if dp[i-1][j] == -1:
            continue
        tmp = j+k
        if tmp > 100:
            tmp =100
        dp[i][tmp] = max(dp[i][tmp], dp[i-1][j])

        if j<h[i]:
            continue
        idx = j - h[i]
        idx += k
        if idx >100:
            idx =100

        dp[i][idx] = max(dp[i-1][j] + s[i],  dp[i][idx])

ans = max(dp[n-1])
if ans == -1:
    ans = 0
print(ans)