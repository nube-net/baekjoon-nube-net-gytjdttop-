import heapq
import sys
input = sys.stdin.readline

def prim(n, G):
    used = [False for _ in range(n)]
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
        for (neigh_weight, neigh_node) in G[node]:
            if not used[neigh_node]:
                heapq.heappush(pq, (neigh_weight, neigh_node))
    return total_weight if count == n else -1


n = int(input())
G = [[] for _ in range(n)]
loc = [list(map(float, input().split())) for _ in range(n)]
for a in range(n):
    for b in range(n):
        if a==b:
            continue
        c = ((loc[a][0]-loc[b][0])**2 +(loc[a][1]-loc[b][1])**2)**0.5

        G[a].append((c, b))
        G[b].append((c, a))

ans = prim(n, G)
print("{:.2f}".format(ans))
