import sys
from heapq import heappop, heappush
inputF = sys.stdin.readline

def code(K):  # 다익스트라(큐)

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

# 입력
N, E = map(int, inputF().split())  # 노드, 간선

Q = []  # 큐
distance = [float('inf') for _ in range(N+1)]
graph = [[] for _ in range(N+1)]  # 간선 양방향 저장
for _ in range(E):
    x, y, z = map(int, inputF().split())
    graph[x].append((z, y))  # 거리 , 노드
    graph[y].append((z, x))
a, b = map(int, inputF().split())  # 경유 노드

dis = list(distance)
# 계산
result = 0
result1 = 0

code(1)
result += distance[a]
result1 += distance[b]
distance = list(dis)

code(a)
result += distance[b]
result1 += distance[N]
distance = list(dis)

code(b)
result += distance[N]
result1 += distance[a]


result = min(result, result1)
if result == float('inf'):
    print(-1)
else:
    print(result)
