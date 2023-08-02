import sys
from heapq import heappop, heappush
inputF = sys.stdin.readline

V, E = map(int, inputF().split())  # 노드 개수, 간선 개수
K = int(inputF())  # 시작 노드

Q = []  # 큐
distance = [float('inf') for _ in range(V+1)]
distance[K] = 0
graph = [[] for _ in range(V+1)]  # 간선 단방향 저장
for _ in range(E):
    x, y, d = map(int, inputF().split())  # 출발, 도착, 가중치
    graph[x].append((d, y))  # 거리 , 노드

Q.append((0,K))
while Q:
    d, x = heappop(Q)
    if d > distance[x]:
        continue
    for line in graph[x]:
        tmp = distance[x] + line[0]
        if tmp < distance[line[1]]:
            distance[line[1]] = tmp
            heappush(Q, (tmp, line[1]))

for i in range(1,V+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])