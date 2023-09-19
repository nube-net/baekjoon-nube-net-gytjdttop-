import sys
input = sys.stdin.readline

n = int(input())
line = list(map(int, input().split()))
a = sum(line[1:n-1]) + max(line[1:n-1])
dp = [0] * n
dp[0] = line[0]

for i in range(1, n):
    dp[i] = dp[i-1] + line[i]

b = 0
for i in range(1, n-1):
    b = max(b, dp[n-2] + dp[i-1] - line[i])

dp2 = [0] * n
dp2[-1] = line[-1]

for i in range(n-2, -1, -1):
    dp2[i] = dp2[i+1] + line[i]

c = 0
for i in range(n-2, 0, -1):
    c = max(c, dp2[1] + dp2[i+1] - line[i])  

print(max(a, b, c))
