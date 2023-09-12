import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
Map = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

S = set()
for _ in range(k):
    x, y = map(int, input().split())
    Map[x-1][y-1] = 1
    S.add((x-1,y-1))

Q = deque()
dx = [1,-1,0,0]
dy = [0,0,-1,1]
ans = 0
while S:
    cnt = 0
    tmp = S.pop()
    Q.append(tmp)
    visited[tmp[0]][tmp[1]] = True

    while Q:
        for __ in range(len(Q)):
            x,y = Q.popleft()
            cnt += 1
            for i in range(4):
                X, Y = x+dx[i], y+dy[i]

                if X < 0 or X >= n or Y < 0 or Y >= m or visited[X][Y]:
                    continue

                if (X,Y) in S:
                    S.remove((X, Y))
                    visited[X][Y] = True
                    Q.append((X,Y))
    ans = max(cnt, ans)
print(ans)