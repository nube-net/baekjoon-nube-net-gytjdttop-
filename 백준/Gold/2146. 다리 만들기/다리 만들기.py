import sys
from collections import deque
input = sys.stdin.readline

def bfs(X, Y):
    Q = deque()
    Q.append((X, Y))
    tmp = set()
    visited[X][Y] = True

    while Q:
        a, b = Q.popleft()
        is_boundary = False
        for i in range(4):
            A, B = a + dx[i], b + dy[i]
            if A < 0 or B < 0 or A >= n or B >= n or visited[A][B]:
                continue
            if Map[A][B] == 1:
                Q.append((A, B))
                visited[A][B] = True
            else:
                is_boundary = True

        if is_boundary:
            tmp.add((a, b, True))
        else:
            tmp.add((a, b, False))

    return tmp


n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]

block = []  # 영역 구분
visited = [[False for _ in range(n)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        if Map[i][j] == 1 and not visited[i][j]:
            block.append(bfs(i, j))

ans = float('inf')
for s in range(len(block)-1):
    Q = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    for a,b,c in block[s]:
        visited[a][b] = True
        if c:
            Q.append((a,b))
    cnt = 0  # 거리 - 1 = 다리 길이
    key = False
    while Q:
        cnt += 1
        l = len(Q)
        for _ in range(l):
            X, Y = Q.popleft()

            for i in range(4):
                x, y = X+dx[i], Y+dy[i]

                if x < 0 or y < 0 or x >= n or y >= n:
                    continue

                if not visited[x][y]:
                    visited[x][y] = True

                    if Map[x][y] == 0:
                        Q.append((x, y))
                    else:
                        ans = min(ans, cnt-1)
                        key = True
        if key:
            break
print(ans)
