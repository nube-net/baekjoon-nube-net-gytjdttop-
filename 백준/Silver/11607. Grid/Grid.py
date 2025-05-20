import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
tmp = [[0 for _ in range(m) ] for _ in range(n)]
visited = [[False for _ in range(m) ] for _ in range(n)]
q = deque()
q.append((0, 0, 0))
visited[0][0] = True

dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

while q:
    x, y, dist = q.popleft()

    k = a[x][y]
    for i in range(4):
        nx = x + dx[i]*k
        ny = y + dy[i]*k

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny, dist + 1))
            if (nx, ny) == (n - 1, m - 1):
                print(dist+1)
                exit()

print("IMPOSSIBLE")
