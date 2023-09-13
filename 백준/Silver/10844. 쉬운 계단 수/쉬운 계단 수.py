import sys
import copy

n=int(sys.stdin.readline())

dp = [0,1,1,1,1,1,1,1,1,1]
for _ in range(n-1):
    tmp = [0]*10
    tmp[0] = dp[1]
    tmp[9] = dp[8]
    for i in range(1,9):
        tmp[i] = dp[i-1]+dp[i+1]
    dp = copy.deepcopy(tmp)


print(sum(dp)%1000000000)

