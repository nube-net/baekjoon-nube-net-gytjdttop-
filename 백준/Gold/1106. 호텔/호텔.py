import sys
input = sys.stdin.readline

c, n = map(int, input().split()) 
tmp = [list(map(int, input().split())) for _ in range(n)] 
dp = [1e7 for _ in range(c+100)]
dp[0] = 0

for i in range(n):
    cost, customers = tmp[i]
    for j in range(customers, c+100): 
        dp[j] = min(dp[j],dp[j-customers]+cost) 

print(min(dp[c:]))
