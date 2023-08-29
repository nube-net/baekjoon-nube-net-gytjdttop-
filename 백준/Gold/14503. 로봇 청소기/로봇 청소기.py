import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())  # 행, 열
x, y, d = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]
idx = d
ans = 0
while True:
    # 1
    if Map[x][y] == 0:
        Map[x][y] = 2
        ans += 1
    # 2, 3
    if 0 in [Map[x+dx[i]][y+dy[i]] for i in range(4)]:  # 3
        for _ in range(4):
            idx -= 1
            if idx < 0:
                idx =3
            if Map[x+dx[idx]][y+dy[idx]] == 0:
                x += dx[idx]
                y += dy[idx]
                break
    else:  # 2
        if Map[x+ dx[(idx+2)%4]][y+dy[(idx+2)%4]] == 1:
            break
        else:
            x = x + dx[(idx+2)%4]
            y = y + dy[(idx+2)%4]
print(ans)