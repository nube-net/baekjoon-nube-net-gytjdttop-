import sys
from heapq import heappop, heappush
inputF = sys.stdin.readline

def code(K):
    distance[K] = 0
    Q = []
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


V, m, E = map(int, inputF().split())
price = list(map(int, inputF().split()))
distance = [float('inf') for _ in range(V+1)]
distance_tmp = list(distance)
graph = [[] for _ in range(V+1)]  # 간선 단방향 저장
for _ in range(E):
    x, y, z = map(int, inputF().split())  # 출발, 도착, 가중치
    graph[x].append((z, y))  # 거리 , 노드
    graph[y].append((z, x))

result = 0
for i in range(1,V+1):
    code(i)
    store = 0
    for k in range(1, V+1):
        if distance[k] <= m:
            store += price[k-1]
    result = max(result, store)
    distance = list(distance_tmp)
print(result)


