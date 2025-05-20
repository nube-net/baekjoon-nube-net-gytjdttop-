import sys
input = sys.stdin.readline

n,m= map(int, input().split())
ans = 0
cost = [[0]*n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0

for _ in range(m):
    x, y= map(int, input().split())
    cost[x-1][y-1] =1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if cost[i][k] and cost[k][j]:
                cost[i][j] = 1

for i in range(n):
    cnt = 0
    for j in range(n):
        if cost[i][j]or cost[j][i]:
            cnt +=1
    if cnt == n-1:
        ans +=1
print(ans)
