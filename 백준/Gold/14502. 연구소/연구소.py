import sys
from collections import deque
from itertools import combinations
import copy

inputF = sys.stdin.readline

# 입력
n, m = map(int, inputF().split())
Map = [list(map(int, inputF().split())) for _ in range(n)]

# 세팅
Q_ = deque()
safety = [m*n]
cases = set()
visited = [[False]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(m):
        if Map[i][j] == 2:
            Q_.append((i, j))
            visited[i][j] = True
            safety[0] -= 1
        elif Map[i][j] == 1:
            visited[i][j] = True
            safety[0] -= 1
        else:
            cases.add((i, j))

aaa = safety[0]
result = 0
for case in list(combinations(cases, 3)):
    aaa = safety[0]
    tmp = copy.deepcopy(visited)
    for x, y in case:
        tmp[x][y] = True
        aaa -= 1
    Q = deque(Q_)

    # BFS
    while Q:
        x, y = Q.popleft()

        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if X < 0 or Y < 0 or X >= n or Y >= m:
                continue
            if not tmp[X][Y]:
                tmp[X][Y] = True
                Q.append((X, Y))
                aaa -= 1
    result = max(result, aaa)

print(result)