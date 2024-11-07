from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
Map = [list(input()) for _ in range(n)]
visited = [[[False]*m for _ in range(n)] for _ in range(2)]
Q = deque()
Q.append((0, 0, 0))
visited[0][0][0] = True
cnt = 1
dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]
if n+m ==2:
    print(1)
    exit()
while Q:
    cnt += 1
    l = len(Q)
    for _ in range(l):
        x, y, z = Q.popleft()

        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if (X < 0) or (X >= n) or (Y < 0) or (Y >= m):  # 범위 초과
                continue
            if visited[z][X][Y]:  # 방문 여부
                continue
            else:
                if Map[X][Y] == '0':  # 이동 가능 하면
                    Q.append((X, Y, z))  # Q 저장
                    visited[z][X][Y] = True
                else:  # 벽 일때
                    if z == 0:  # 부술 수 있을 때
                        for j in range(4):
                            if X + dx[j] < 0 or X + dx[j] >= n or Y+dy[j] < 0 or Y+dy[j] >= m:  # 범위 초과
                                continue

                            if not visited[1][X+dx[j]][Y+dy[j]]:  # 방문 안 했으면
                                if Map[X+dx[j]][Y+dy[j]] == '0':
                                    Q.append((X+dx[j], Y+dy[j], 1))
                                    visited[1][X+dx[j]][Y+dy[j]] = True
    if visited[0][n - 1][m - 1] or visited[1][n - 1][m - 1]:
        break

if visited[0][n-1][m-1] or visited[1][n-1][m-1]:
    if visited[1][n-1][m-1]:
        print(cnt+1)
    else:
        print(cnt)
else:
    print(-1)