import sys
input = sys.stdin.readline

class DSU: # Dsu 템플릿2
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)
    def find(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]] 
            a = self.parent[a]
        return a

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

n, m = map(int, input().split())
dsu = DSU(n)

g = [set() for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    g[x].add(y)
    g[y].add(x)

cur = n + 1
idx = -1
for i in range(1, n + 1):
    if len(g[i]) < cur:
        idx = i
        cur = len(g[i])
S2 = g[idx]

for i in range(1, n + 1):
    if i in S2:
        continue
    dsu.union(idx, i)

for i in range(1, n + 1):
    for j in S2:
        if j in g[i]:
            continue
        dsu.union(i, j)

cnt = {}
for i in range(1, n + 1):
    root = dsu.find(i)
    cnt[root] = cnt.get(root, 0) + 1

ans = sorted(cnt.values())
print(len(ans))
print(*ans)
