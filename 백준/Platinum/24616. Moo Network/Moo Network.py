import sys
import heapq
input = sys.stdin.readline
# 10000*100000 // 100000 10000(99*99)
def prim(n, G):
    used = [False] * n
    pq = [(0, 0)]
    total_weight = 0
    count = 0
    while pq:
        weight, node = heapq.heappop(pq)
        if used[node]:
            continue
        used[node] = True
        total_weight += weight
        count += 1
        for neigh_weight, neigh_node in G[node]:
            if not used[neigh_node]:
                heapq.heappush(pq, (neigh_weight, neigh_node))
    return total_weight if count == n else -1

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
a.sort()

G = [[] for _ in range(n)]
for i in range(n):
    for j in range(max(0, i - 99), min(n, i + 99)):
        if i == j:
            continue
        tmp = (a[i][0] - a[j][0])**2 + (a[i][1] - a[j][1])**2
        G[i].append((tmp, j))

print(prim(n, G))
