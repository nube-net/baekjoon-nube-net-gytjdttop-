import sys
inputF = sys.stdin.readline

n = int(inputF())

graph = [list(map(int, inputF().split())) for _ in range(n)]

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            for k in range(n):
                if graph[k][x] == 1:
                    if graph[k][y] == 0:
                        graph[k][y] = 1

for l in graph:
    print(*l)