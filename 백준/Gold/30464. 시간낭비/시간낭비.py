import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def code(r, p, q):
    if r < 1 or r > n:
        return float('-inf')
    
    if r == n:
        return 0
    
    if not dp[r][p][q]:
        dp[r][p][q] = float('-inf')
        if p == 0:
            dis = a[r]
        else:
            dis = - a[r]
        dp[r][p][q] = max(dp[r][p][q], code(r + dis, p, q) + 1)
        if q < 2:
            P = 1 - p
            dp[r][p][q] = max(dp[r][p][q], code(r - dis, P, q + 1) + 1)
    return dp[r][p][q]


n = int(input().strip())
a = [0] + list(map(int, input().split()))

dp = [[[False for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

ans = code(1, 0, 0)
if ans > 0:
    print(ans)
else:
    print(-1)


