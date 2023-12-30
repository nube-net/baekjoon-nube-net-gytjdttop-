import heapq
import sys
input = sys.stdin.readline

t = 1
for __ in range(t):
    n, m = map(int, input().split())
    tmp1 = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    tmp = [list(map(int, input().split())) for i in range(m)]
    # tmp1 = list(map(int, input().split()))
    for a,b,c in tmp:
        graph[a - 1].append((b - 1, c*(tmp1[a-1])))
        graph[b - 1].append((a - 1, c * (tmp1[b - 1])))

    dist = [float("inf") for _ in range(n)]
    pq = []

    start = 0  # 시작 노드
    heapq.heappush(pq, (0, start))
    dist[start] = 0  # The shortest path from a node to itself is 0
    while pq:
        cdist, node = heapq.heappop(pq)
        if cdist != dist[node]:
            continue

        for i in graph[node]:
            if cdist + i[1] < dist[i[0]]:
                dist[i[0]] = cdist + i[1]
                heapq.heappush(pq, (dist[i[0]], i[0]))

    print(dist[n-1])