import sys
from heapq import heappop, heappush
inputF = sys.stdin.readline

def code(K):
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
                Map[line[1]] = x ###


a, b = map(int, inputF().split())
Q = []  # 큐
distance = [float('inf') for _ in range(200001)]
graph = [[] for _ in range(200001)]

for i in range(0, 100001):
    graph[i].append((1, i-1))
    graph[i].append((1, i + 1))
    graph[i].append((1, 2*i))
Map = [0] * (200001) #
code(a)
print(distance[b])
#####
s = [b]
while b != a:
    tmp = Map[b]
    b = tmp
    s.append(tmp)
s.reverse()
print(*s)

