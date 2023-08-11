import sys
k,n=map(int, sys.stdin.readline().split())
dp =[0]*(n+k+1)
dp[k] = 1
for _ in range(n):
    a=[0]+dp[2:]+[0]
    b=[0,0]+dp[1:]
    dp=[x+y for x,y in zip(a,b)]
print(sum(dp[1:]))
