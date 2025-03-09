import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int,input().split())
a = [list(input().rstrip()) for _ in range(r)]
tmp = []
for i in range(r):
    for j in range(c):
        if a[i][j] == 'L':
            tmp.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans =0
for st in tmp:
    visit = [[False for _ in range(c)] for _ in range(r)]
    q = deque([st])
    visit[st[0]][st[1]] = True
    cnt = 0
    k = False
    while q:
        cnt += 1
        l = len(q)
        for _ in range(l):
            x,y = q.popleft()
            
            for i in range(4):
                X, Y = x+dx[i], y+dy[i]
                if X < 0 or X >= r or Y <0 or Y >= c or visit[X][Y] or a[X][Y]=='W':
                    continue
                k = True
                visit[X][Y] = True
                q.append((X,Y))
    if k:
        #print(st, cnt)
        ans = max(ans, cnt)
print(ans-1)