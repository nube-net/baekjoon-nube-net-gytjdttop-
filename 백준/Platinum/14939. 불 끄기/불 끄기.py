import sys
from itertools import combinations
import copy
input = sys.stdin.readline

Map = [list(input().strip()) for _ in range(10)]
L = 0
for i in range(10):
    for j in range(10):
        if Map[i][j] == '#':
            Map[i][j] = 0
        else:
            Map[i][j] = 1

dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]
ans = float('inf')
num ={0,1,2,3,4,5,6,7,8,9}
for k in range(0,11):
    for S in list(combinations(num, k)):
        S = list(S)
        L += 1
        S.sort()
        a = copy.deepcopy(Map)
        cnt = 0

        for i in S:
            cnt += 1
            a[0][i] = abs(a[0][i]-1)
            for j in range(4):
                if dx[j] < 0 or dx[j] > 9 or i+dy[j] < 0 or i+dy[j] > 9:
                    continue
                a[dx[j]][i+dy[j]] = abs(a[dx[j]][i+dy[j]] - 1)

        for x in range(1,10):
            for y in range(10):
                if a[x-1][y] == 1:
                    cnt += 1
                    a[x][y] = abs(a[x][y]-1)

                    for i in range(4):
                        X, Y = x+dx[i], y+dy[i]
                        if X < 0 or X > 9 or Y <0 or Y > 9:
                            continue

                        a[X][Y] = abs(a[X][Y]-1)

        tmp = 0
        for p in a:
            tmp += sum(p)
        if tmp == 0:
            ans = min(ans, cnt)
if ans == float('inf'):
    ans = -1
print(ans)
#print(L)