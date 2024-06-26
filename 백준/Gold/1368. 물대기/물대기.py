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
G = [[] for _ in range(n+1)]
for _ in range(n):
    tmp = int(input())
    G[0].append((tmp,_+1))
    G[_+1].append((tmp, 0))
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        if j==i:
            continue
        G[j+1].append((a[j],i+1))
        G[i + 1].append((a[j], j + 1))
ans = prim(n+1, G)
print(ans)
