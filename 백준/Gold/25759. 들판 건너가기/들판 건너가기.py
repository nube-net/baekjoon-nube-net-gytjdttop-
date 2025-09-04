import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
d = max(a)
dp = [-1 for _ in range(d+1)]

for i in range(n):
    cur = a[i]
    new_dp = dp[:]  
    if new_dp[cur] == -1:
        new_dp[cur] = 0 
    for j in range(1, d+1):
        if dp[j] != -1:  
            new_dp[cur] = max(new_dp[cur], dp[j] + (cur - j)**2)
    dp = new_dp  

print(max(dp))
