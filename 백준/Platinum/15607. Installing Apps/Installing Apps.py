import sys

input = sys.stdin.readline

n, c = map(int, input().split())  # app, memory
arr = []
for i in range(n):
    d, s = map(int, input().split())
    arr.append((d, s, i + 1))
arr.sort(key=lambda x: -(x[0] - x[1]))

INF = 10**18
dp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0] = 0
used = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    d, s, idx = arr[i - 1]
    dp[i][0] = 0

    for j in range(1, i + 1):
        if dp[i - 1][j] < dp[i][j]:
            dp[i][j] = dp[i - 1][j]
            used[i][j] = 0

        if dp[i - 1][j - 1] <= c - max(d, s):
            cand = dp[i - 1][j - 1] + s
            if cand < dp[i][j]:
                dp[i][j] = cand
                used[i][j] = 1

ans = 0
for i in range(n, -1, -1):
    if dp[n][i] <= c:
        ans = i
        break

print(ans)
if ans:
    tmp = []
    k = ans
    for i in range(n, 0, -1):
        if k <= 0:
            break
        if used[i][k]:
            tmp.append(arr[i - 1][2])
            k -= 1
    tmp.reverse()
    print(*tmp)
