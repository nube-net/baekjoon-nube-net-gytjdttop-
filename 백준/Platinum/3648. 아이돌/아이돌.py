import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def xtoidx(x, n):
    if x < 0:
        return abs(x) + n
    return x

def notx(x, n):
    if x > n:
        return x - n
    return x + n

def dfs1(v, adj, vis, order):
    vis[v] = True
    for u in adj[v]:
        if not vis[u]:
            dfs1(u, adj, vis, order)
    order.append(v)

def dfs2(v, rev_adj, vis, comp_id, label):
    vis[v] = True
    comp_id[v] = label
    for u in rev_adj[v]:
        if not vis[u]:
            dfs2(u, rev_adj, vis, comp_id, label)

while True:
    line = input()
    if not line:
        break
    try:
        n, m = map(int, line.strip().split())
    except:
        break

    L = 2 * n + 1
    adj = [[] for _ in range(L)]
    rev_adj = [[] for _ in range(L)]

    for _ in range(m):
        a, b = map(int, input().split())
        a = xtoidx(a, n)
        b = xtoidx(b, n)
        na = notx(a, n)
        nb = notx(b, n)
        adj[na].append(b)
        adj[nb].append(a)
        rev_adj[b].append(na)
        rev_adj[a].append(nb)

    adj[n + 1].append(1)
    rev_adj[1].append(n + 1)

    order = []
    vis = [False] * L
    for i in range(1, L):
        if not vis[i]:
            dfs1(i, adj, vis, order)

    vis = [False] * L
    comp_id = [0] * L
    label = 0
    for i in reversed(order):
        if not vis[i]:
            label += 1
            dfs2(i, rev_adj, vis, comp_id, label)

    is_conflict = False
    for i in range(1, n + 1):
        if comp_id[i] == comp_id[notx(i, n)]:
            print("no")
            is_conflict = True
            break
    if not is_conflict:
        print("yes")
