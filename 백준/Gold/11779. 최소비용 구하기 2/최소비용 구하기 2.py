import sys
from heapq import heappop, heappush

inputF = sys.stdin.readline

def code(K):  # 다익스트라
    distance[K] = 0
    Q.append((0, K))
    while Q:
        d, x = heappop(Q)
        if d > distance[x]:
            continue
        for line in graph[x]:
            tmp = distance[x] + line[0]
            if tmp < distance[line[1]]:
                distance[line[1]] = tmp
                heappush(Q, (tmp, line[1]))
                Map[line[1]] = x

V = int(inputF())
E = int(inputF())
Q = []
distance = [float('inf') for _ in range(V + 1)]
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    x, y, z = map(int, inputF().split())
    graph[x].append((z, y))

Map = [0] * (V + 1)
K, O = map(int, inputF().split())
code(K)
print(distance[O])

s = [O]
while O != K:
    tmp = Map[O]
    O = tmp
    s.append(tmp)
s.reverse()
print(len(s))
print(*s)
