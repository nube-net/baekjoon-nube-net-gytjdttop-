import sys
from collections import deque
inputF = sys.stdin.readline

# 입력
n, l, r = map(int, inputF().split())
Map = [list(map(int, inputF().split())) for _ in range(n)]

# 세팅
team = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
non_visited = set()  # 미방문 좌표 원본
for i in range(n):
    for j in range(n):
        non_visited.add((i, j))

# BFS
while True:
    Q = deque()
    no_visit = set(non_visited) # 미방문 좌표

    while no_visit:
        tmp = [[], 0]  # 연합 좌표, 인구 수 합
        Q.append(no_visit.pop())  # 무작위 위치 부터 탐색)
        while Q:
            country = Q.popleft()

            tmp[0].append(country)
            tmp[1] += Map[country[0]][country[1]]
            for i in range(4):
                X, Y = country[0] + dx[i], country[1] + dy[i]
                if X < 0 or X >= n or Y < 0 or Y >= n:
                    continue
                if (X, Y) in no_visit:
                    if l <= abs(Map[country[0]][country[1]] - Map[X][Y]) <= r:
                        no_visit.remove((X, Y))
                        Q.append((X, Y))
        if len(tmp[0]) > 1:
            team.append(tmp)

    if not team:  # 연합 미생성 시 인구 이동 없음
        break
    else:
        while team:
            locations, points = team.pop()
            point = points//len(locations)
            for x, y in locations:
                Map[x][y] = point
        cnt += 1

# 출력
print(cnt)