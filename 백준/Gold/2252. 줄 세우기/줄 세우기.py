import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

Q = deque()
graph = [[] for _ in range(n+1)]
taller = [0 for _ in range(n+1)]
result = []
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    taller[y] += 1

for i in range(1, n+1):
    if taller[i] == 0:
        Q.append(i)

while Q:
    tmp = Q.popleft()
    result.append(tmp)
    for k in graph[tmp]:
        taller[k] -= 1
        if taller[k] == 0:
            Q.append(k)
    graph[tmp] = []

print(*result)