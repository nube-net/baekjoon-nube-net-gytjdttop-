import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
cur = [list(map(int, input().split())) for _ in range(r)]
arr = [list(map(int, input().split())) for _ in range(r)]

cur_o = [(0, 0) for _ in range(r * c + 1)]
arr_o = [(0, 0) for _ in range(r * c + 1)]
for i in range(r):
    for j in range(c):
        arr_o[arr[i][j]] = (i, j)
        cur_o[cur[i][j]] = (i, j)
ans = []
q = deque([])
for i in range(r * c, 0, -1):
    if cur_o[i] == arr_o[i]:
        continue
    x, y = cur_o[i]
    q.append([x, y])

    X, Y = arr_o[i]
    for j in range(y - 1, -1, -1):
        if cur[X][Y] < cur[x][j]:
            q.append([x, j])
        else:
            break

    while q:
        tmp_x, tmp_y = q.pop()
        ans.append([X + 1, Y + 1, tmp_x + 1, tmp_y + 1])

        cur[X][Y], cur[tmp_x][tmp_y] = cur[tmp_x][tmp_y], cur[X][Y]

        cur_o[cur[X][Y]] = (X, Y)
        cur_o[cur[tmp_x][tmp_y]] = (tmp_x, tmp_y)

print(len(ans))
for i in ans:
    print(*i)
