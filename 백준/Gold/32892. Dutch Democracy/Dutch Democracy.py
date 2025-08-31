import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
l = sum(a)
x = l//2+1
dp = [0 for _ in range(x)]
ans = 0

dp[0] = 1
for i in range(n):
    cur = a[i]
    for j in range(x-1,-1,-1):
        if dp[j] >0:
            if j+cur < x:
                dp[j+cur] += dp[j]
            else:
                ans+= dp[j]
            
print(ans)

