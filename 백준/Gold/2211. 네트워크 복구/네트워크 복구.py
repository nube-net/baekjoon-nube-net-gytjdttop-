import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

dist = [sys.maxsize for _ in range(n)]
pq = []
ans = [0 for _ in range(n)]
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
            ans[i[0]] = node
print(n-1)
for i in range(1,n):
    print(i+1, ans[i]+1)