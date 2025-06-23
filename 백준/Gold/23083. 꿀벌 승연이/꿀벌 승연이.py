import sys
input = sys.stdin.readline

n, m = map(int,input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
k = int(input())
for _ in range(k):
    r,c = map(int,input().split())
    a[r-1][c-1] = -1
tmp = 1000000007
a[0][0] = 1
dx = [[-1,-1,0], [-1,0,1]]
dy = [[0,-1,-1], [0,-1,-1]]
for j in range(m):
    for i in range(n):
        if a[i][j] == -1:
            continue
            
        for k in range(3):
            x,y = i+dx[j%2][k], j+dy[j%2][k]
            if 0<=x<n and 0<=y<m and a[x][y] != -1:
                a[i][j] += a[x][y]
                a[i][j] %=tmp

print(a[n-1][m-1])



