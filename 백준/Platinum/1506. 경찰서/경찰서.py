import sys
input = sys.stdin.readline

def dfs(u, n):
    ret = cost[u]
    visited[u] = True
    for i in range(n):
        if not visited[i] and c[u][i] and c[i][u]:
            ret = min(ret, dfs(i, n))
    return ret

n = int(input())
cost = list(map(int, input().split()))
c = [[0]*n for _ in range(n)]
visited = [False]*n

for i in range(n):
    s = input().rstrip()
    for j in range(n):
        if s[j] == '1':
            c[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if c[i][k] and c[k][j]:
                c[i][j] = 1

ans = 0
for i in range(n):
    if not visited[i]:
        ans += dfs(i, n)

print(ans)
