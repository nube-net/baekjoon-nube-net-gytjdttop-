import sys
n = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))
dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = dp[i-1] + S[i-1]
st = 0
ans = dp[1]
for i in range(n+1):
    if i == 0 or i == 1:
        if dp[st] > dp[i]:
            st = i
        continue
    else:
        ans = max(ans, dp[i]-dp[st])
        if dp[st] > dp[i]:
            st = i
print(ans)