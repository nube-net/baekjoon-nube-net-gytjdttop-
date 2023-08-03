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


a, b = map(int, inputF().split())
Q = []  # 큐
distance = [float('inf') for _ in range(200001)]
graph = [[] for _ in range(200001)]

for i in range(0, 100001):
    graph[i].append((1, i-1))
    graph[i].append((1, i + 1))
    graph[i].append((0, 2*i))

code(a)
print(distance[b])




