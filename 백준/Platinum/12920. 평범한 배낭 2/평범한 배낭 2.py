import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a= []
for _ in range(n):
    v,c,k = map(int, input().split())  # 무게, 효용, 개수
    d = 1
    while k > 0:  # 이진수 반복 분해
        if k < d:
            d = 1
            continue
        else:
            k -= d
            a.append((v*d,c*d))
        d *= 2
dp = [-1 for _ in range(m+1)]
dp[0] = 0
for v, c in a:
    for i in range(m,v-1,-1):
        if dp[i-v] != -1:
            dp[i] = max(dp[i-v]+c, dp[i])
print(max(dp))