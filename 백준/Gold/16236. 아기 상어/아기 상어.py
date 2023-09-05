import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]
size = 2  # 초기 사이즈
grow = size  # 성장을 위한 필요 먹이(현재 사이즈)
dx = [-1, 0, 0, 1]  # 상 좌 우 하
dy = [0, -1, 1, 0]
tmp = [[0 for _ in range(n)] for _ in range(n)]
visited = copy.deepcopy(tmp)
# 이동 시 BFS
Q = deque()
for i in range(n):
    for j in range(n):
        if Map[i][j] == 9:
            Q.append((i, j))
            Map[i][j] = 0
            visited[i][j] = 1
            break

ans = 0
while Q:
    Feed = set()  # 먹이 위치 저장
    cnt = 0

    while Q:  # 먹이 탐색
        cnt += 1
        L = len(Q)  # 순회 기준

        for __ in range(L):
            x, y = Q.popleft()  # 위치, 이동 횟수

            for _ in range(4):
                X, Y = x + dx[_], y + dy[_]
                if X < 0 or Y < 0 or X >= n or Y >= n:
                    continue

                if visited[X][Y] == 0:
                    if Map[X][Y] <= size:  # 현재 보다 작거나 같은 크기(또는 빈 칸)
                        Q.append((X, Y))
                        visited[X][Y] = 1
                        if Map[X][Y] != 0:
                            if Map[X][Y] < size:
                                Feed.add((X, Y))
                    else:
                        visited[X][Y] = 1

        if Feed:  # 먹이 존재 시
            Feed = sorted(Feed)
            x, y = Feed[0]  # 같은 거리일 시 조건에 맞는 먹이 추출
            Map[x][y] = 0
            grow -= 1
            ans += cnt
            if grow == 0:
                size += 1
                grow = size
            Q = deque()
            Q.append((x, y))
            break
    visited = copy.deepcopy(tmp)
    if Q:
        x, y = Q.popleft()
        visited[x][y] = 1
        Q.append((x, y))

print(ans)