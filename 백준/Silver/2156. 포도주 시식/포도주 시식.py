import sys
import copy
input = sys.stdin.readline

n = int(input())
dp = [0]*4
for _ in range(n):
    tmp = [0]*4
    unit = int(input())
    tmp[0] = max(dp[2], dp[3]) + unit
    tmp[1] = dp[0] + unit
    tmp[2] = max(dp[0], dp[1])
    tmp[3] = dp[2]
    dp = list(tmp)
print(max(dp))
