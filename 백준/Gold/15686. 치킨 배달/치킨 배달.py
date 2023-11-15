import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
          chicken.append((i,j))
        if a[i][j] == 1:
            house.append((i,j))
ans = sys.maxsize
for selected in list(combinations(chicken, m)):
    Q = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    houses = set(house)
    for x,y in selected:
        visited[x][y] = True
        Q.append([x,y])
    tmp = 0
    cnt = 0
    while houses:
        l = len(Q)
        cnt += 1
        for _ in range(l):
            x, y = Q.popleft()
            for i in range(4):
                X, Y = x+dx[i], y+dy[i]
                if X <0 or Y <0 or X >= n or Y >= n:
                    continue
                if visited[X][Y]:
                    continue
                Q.append((X,Y))
                visited[X][Y] = True
                if (X,Y) in houses:
                    tmp += cnt
                    houses.remove((X,Y))
    ans = min(ans,tmp)
print(ans)



