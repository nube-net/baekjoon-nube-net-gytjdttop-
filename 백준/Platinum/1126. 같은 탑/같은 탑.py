import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
L = sum(a)
dp = [[-1] * (L+1) for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    bloc = a[i]
    for j in range(L, -1, -1):
        max_h = dp[i][j]
        if max_h == -1:
            continue
        # 그대로 유지
        dp[i+1][j] = max(dp[i+1][j], max_h)
        # 큰 탑에 추가
        if j + bloc <= L:
            dp[i+1][j+bloc] = max(dp[i+1][j+bloc], max_h + bloc)
        # 작은 탑에서 블록 제거
        if j >= bloc:
            dp[i+1][j-bloc] = max(dp[i+1][j-bloc], max_h)
        else:
            dp[i+1][bloc-j] = max(dp[i+1][bloc-j], max_h + (bloc-j))

ans = dp[n][0]
print(-1 if ans <= 0 else ans)
