import sys

n, m = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

edge = [-1]*n  # 끝점 저장
for i in range(n):
    for j in range(m-1, -1,-1):
        if Map[i][j] == 1:
            edge[i] = j
            break
cnt = 0
for i in range(n):
    index = edge[i]
    if index == -1:
        continue

    cnt +=1
    if i != n-1:
        for j in range(i+1, n):
            if edge[j] >= index:
                tmp = edge[j]
                for k in range(index, m):
                    Map[j][k] = 0

                for k in range(index, -1, -1):
                    if Map[j][k] == 1:
                        edge[j] = k
                        break
                    if k == 0:
                        edge[j] = -1
                index = tmp

print(cnt)