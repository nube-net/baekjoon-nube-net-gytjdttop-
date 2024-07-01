import sys
from collections import  deque
input = sys.stdin.readline

n,m = map(int,input().split())
a = [list(input().rstrip()) for _ in range(n)]
q = deque()
dic = {}
check = [[[False for _ in range(m)]for _ in range(n)]for _ in range(4)]
for i in range(n):
    for j in range(m):
        if a[i][j] == "S":
            for k in range(4):
                q.append((i,j,k))
        elif a[i][j] == "#":
            for k in range(4):
                check[k][i][j] = True

q2 = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0
flag = True
cnt = 0
while q and flag:
    cnt += 1
    l = len(q)
    for _ in range(l):
        r,c,d = q.popleft()
        for i in range(4):
            x, y = r+dx[i], c+dy[i]
            if x <0 or y<0 or x>=n or y >= m or check[i][x][y] or d ==i:
                continue

            check[i][x][y] = True
            if a[x][y] == "C":
                flag = False
                q2.append((x, y, i,x*m + y))
                ans = cnt
                if x*m+y not in dic:
                    dic[x*m+y] = [[[False for _ in range(m)]for _ in range(n)]for _ in range(4)]
            else:
                q.append((x, y, i))
#print(ans)
cnt = 0
q2 =deque(q2)
while q2:
    cnt += 1
    l = len(q2)
    #print(q2)
    for _ in range(l):
        r,c,d,visit = q2.popleft()
        #print(r,c,d,visit," :")
        for i in range(4):
            x, y = r+dx[i], c+dy[i]
            if x <0 or y<0 or x>=n or y >= m or dic[visit][i][x][y] or d ==i or a[x][y] == "#":
                continue
            dic[visit][i][x][y] = True
            #print(x,y)
            if a[x][y] == "C" and x*m+y != visit:
                print(ans+cnt)
                exit()
            else:
                q2.append((x, y, i,visit))
    #print()
print(-1)
