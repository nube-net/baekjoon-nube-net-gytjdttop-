import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
a = [list(input().rstrip()) for _ in range(m)]
visited = [[False for _ in range(n)]for _ in range(m)]
ans = [0, 0]
q = deque()
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(m):
    for j in range(n):
        if visited[i][j]:
            continue
        cur = a[i][j]
        q.append([i,j])
        visited[i][j] = True
        tmp = 0
        while q:
            x,y = q.popleft()
            tmp += 1
            for k in range(4):
                X,Y = x+dx[k], y+dy[k]
                if X <0 or Y <0 or X >= m or Y >=n or visited[X][Y] or  a[X][Y] != cur:
                    continue
                
                visited[X][Y]= True
                q.append([X,Y])
        if cur == "W":
            ans[0] += tmp**2
        else:
            ans[1] += tmp**2
print(*ans)

