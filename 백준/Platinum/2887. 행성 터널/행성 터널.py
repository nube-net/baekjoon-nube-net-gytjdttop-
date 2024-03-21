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
def setting(a,idx):
    global  G
    a.sort(key=lambda x: x[idx])
    for i in range(n):
        if i != 0:
            w =abs(a[i][idx] - a[i - 1][idx])
            G[a[i][0]].append((w, a[i - 1][0]))
            G[a[i - 1][0]].append((w, a[i][0]))


n = int(input())
G = [[] for _ in range(n)]
a= []
for i in range(n):
    a.append(([i]+list(map(int,input().split()))))
setting(a,1)
setting(a,2)
setting(a,3)
ans = prim(n, G)
#print(a)
#print(G)
print(ans)
