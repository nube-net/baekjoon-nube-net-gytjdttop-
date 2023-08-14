import sys
from collections import deque
# 위상 정렬, 약간의 너비탐색 응용
n, m = map(int, sys.stdin.readline().split())

Q = deque()
graph = [[] for _ in range(n+1)]
taller = [0 for _ in range(n+1)]
result = [n for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    taller[y] += 1

for i in range(1, n+1):
    if taller[i] == 0:
        Q.append(i)

cnt =1
while Q:
    tmp_Q = []
    while Q:
        tmp = Q.popleft()
        result[tmp] = min(result[tmp], cnt)
        for k in graph[tmp]:
            taller[k] -= 1
            if taller[k] == 0:
                tmp_Q.append(k)
        graph[tmp] = []
    Q = deque(tmp_Q)
    cnt +=1
print(*result[1:])