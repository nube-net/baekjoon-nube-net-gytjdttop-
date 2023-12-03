from collections import deque
from heapq import heappop, heappush, heapify
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
indegree = [0] * n
q =[]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    indegree[b - 1] += 1

for i in range(n):
    if indegree[i] == 0:
        q.append(i)

order = []
heapify(q)
while q:
    #print(q)
    #print(order)

    curr = heappop(q)
    order.append(curr)
    for next_node in graph[curr]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            heappush(q,next_node)


if len(order) != n:
    print("IMPOSSIBLE")
else:
    for node in order:
        print(node + 1, end=' ')
    print()
