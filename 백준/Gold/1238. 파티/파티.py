import sys
from heapq import heappop, heappush
inputF = sys.stdin.readline
# 방향 바꿔서 목표 노드를 시작 노드로 계산
# 시작 노드(원래 목표 노드) 가장 먼 노드 거리 => 해답
def code(X):
    distance[X] = 0  # 시작 노드
    Q = []  # 큐
    heappush(Q, (0, X))
    while Q:
        z, node = heappop(Q)
        if z > distance[node]:
            continue
        for road in graph[node]:
            tmp = road[1] + distance[node]
            if distance[road[0]] > tmp:
                distance[road[0]] = tmp
                heappush(Q, (tmp, road[0]))
def code1(X):
    distance_tmp[X] = 0  # 시작 노드
    Q = []  # 큐
    heappush(Q, (0, X))
    while Q:
        z, node = heappop(Q)
        if z > distance_tmp[node]:
            continue
        for road in graph_tmp[node]:
            tmp = road[1] + distance_tmp[node]
            if distance_tmp[road[0]] > tmp:
                distance_tmp[road[0]] = tmp
                heappush(Q, (tmp, road[0]))

# 입력
N, M, X = map(int, inputF().split())  # 노드 수, 도로 수, 목표 노드(시작 노드)
graph = [[] for _ in range(N+1)]  # 단방향 도로 저장
graph_tmp = [[] for _ in range(N+1)]  # 단방향 도로 저장
for _ in range(M):
    x, y, z = map(int, inputF().split())  # 끝점, 시작점, 소요 시간
    graph[y].append((x, z))
    graph_tmp[x].append((y,z))
distance = [1000001 for _ in range(N+1)]
distance_tmp = [1000001 for _ in range(N+1)]

code(X)
code1(X)
result =0

for i in range(1, N+1):
    result = max(result, distance[i] + distance_tmp[i])

print(result)