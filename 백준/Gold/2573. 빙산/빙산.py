import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
iceberg = [list(map(int,input().split())) for _ in range(n)]
ans = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 1
while cnt > 0:
    tmp = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if iceberg[r][c] == 0:
                continue
            for i in range(4):
                x, y = r + dx[i], c + dy[i]
                if x < 0 or y < 0 or x>=n or y>=m or iceberg[x][y] != 0:
                    continue
                tmp[r][c] += 1

    for r in range(n):
        for c in range(m):
            iceberg[r][c] = max(0, iceberg[r][c]-tmp[r][c])
            if iceberg[r][c] == 0:
                visited[r][c] = True
                
    ans += 1
    q = deque()
    cnt = 0
    for r in range(n):
        for c in range(m):
            if not visited[r][c]:
                cnt += 1
                q.append([r,c])
                visited[r][c] = True
                while q:
                    a = q.popleft()
                    for i in range(4):
                        x,y = a[0]+dx[i], a[1]+dy[i]
                        if x<0 or y<0 or x>=n or y>=m or visited[x][y]:
                            continue
                        q.append([x,y])
                        visited[x][y] = True
    if cnt >= 2:
        print(ans)
        exit()
print(0)
