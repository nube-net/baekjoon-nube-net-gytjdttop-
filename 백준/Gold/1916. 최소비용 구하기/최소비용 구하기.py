import sys
from heapq import heappop, heappush
inputF = sys.stdin.readline

V = int(inputF())  # 노드 개수
E = int(inputF())  # 간선
Q = []  # 큐
distance = [float('inf') for _ in range(V+1)]
graph = [[] for _ in range(V+1)]  # 간선 단방향 저장
for _ in range(E):
    x, y, d = map(int, inputF().split())  # 출발, 도착, 가중치
    graph[x].append((d, y))  # 거리 , 노드

K, O = map(int, inputF().split())  # 시작, 끝 노드
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

print(distance[O])