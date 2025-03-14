import sys
input = sys.stdin.readline


def dfs(cnt):
    global n
    if cnt >= n:
        for i in Map:
            print("".join(map(str, i)))
        exit()
    
    r, c = a[cnt]
    for j in range(1, 10):
        if j in Map[r] or any(Map[x][c] == j for x in range(9)):
            continue

        X, Y = (r // 3) * 3, (c // 3) * 3
        if any(Map[X + x][Y + y] == j for x in range(3) for y in range(3)):
            continue
        
        Map[r][c] = j
        dfs(cnt+ 1)
        Map[r][c] = 0


Map = [list(map(int, input().rstrip())) for _ in range(9)]
a = []
for i in range(9):
    for j in range(9):
        if Map[i][j] == 0:
            a.append((i, j))
n = len(a)
dfs(0)
