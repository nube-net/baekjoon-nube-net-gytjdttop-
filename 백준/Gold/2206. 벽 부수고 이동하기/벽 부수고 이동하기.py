import sys
inputF = sys.stdin.readline

n, m = map(int, inputF().split())
Map = [list(inputF()) for _ in range(n)]
visited = [[[False]*m for _ in range(n)] for _ in range(2)]
Q = set()
Q.add((0, 0, 0))
cnt = 0

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]
while Q:
    cnt +=1
    tmp = set()
    while Q:
        x, y, z = Q.pop()
        visited[z][x][y] = True  # 체크
        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if (X < 0) or (X >= n) or (Y < 0) or (Y >= m):  # 범위 초과
                continue

            if visited[z][X][Y]:  # 방문 여부
                continue
            else:
                if Map[X][Y] == '0':  # 이동 가능 하면
                    tmp.add((X, Y, z))  # Q 저장
                else:  # 벽 일때
                    if z == 0:  # 부술 수 있을 때
                        if X + dx[i] < 0 or X + dx[i] >= n or Y+dy[i] < 0 or Y+dy[i] >= m:  # 범위 초과
                            continue

                        if not visited[1][X+dx[i]][Y+dy[i]]:  # 방문 안 했으면
                            # check
                            if Map[X+dx[i]][Y+dy[i]] == '0':
                                tmp.add((X+dx[i], Y+dy[i], 1))
    Q = set(tmp)
    if visited[0][n - 1][m - 1] or visited[1][n - 1][m - 1]:
        break

if visited[0][n-1][m-1] or visited[1][n-1][m-1]:
    if visited[1][n-1][m-1]:
        print(cnt+1)
    else:
        print(cnt)
else:
    print(-1)