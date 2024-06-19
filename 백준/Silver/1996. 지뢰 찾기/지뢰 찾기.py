import sys
input = sys.stdin.readline
n = int(input())

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

a = [list(input().rstrip()) for _ in range(n)]
ans = [[ "*" for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        cur = a[i][j]
        cnt = 0
        if cur == ".":
            for k in range(8):
                x,y = i+dx[k], j+dy[k]
                if x < 0 or x >=n or y <0 or y>=n:
                    continue
                if a[x][y] != ".":
                    cnt += int(a[x][y])

            if cnt >= 10:
                ans[i][j] = "M"
            else:
                ans[i][j] = str(cnt)
        else:
            continue

for i in ans:
    print("".join(i))
