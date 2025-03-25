import sys

input = sys.stdin.readline


def xtoidx(x):
    if x < 0:
        x = abs(x) + n
    return x


def notx(x):
    global n
    if x > n:
        x -= n
    else:
        x += n
    return x


def dfs1(v: int):
    stack = [v]
    while stack:
        node = stack[-1]
        if not vis[node]:
            vis[node] = True
        finished = True
        for u in adj[node]:
            if not vis[u]:
                stack.append(u)
                finished = False
                break
        if finished:
            order.append(stack.pop())
        else:
            vis[node] = True


def dfs2(x: int, comp: int):
    stack = [x]
    while stack:
        node = stack.pop()
        if not vis[node]:
            vis[node] = True
            comp_id[node] = comp
            for u in rev_adj[node]:
                if not vis[u]:
                    stack.append(u)


m, n = map(int, input().split())
order = []
L = n * 2 + 1
adj = [[] for _ in range(L)]
rev_adj = [[] for _ in range(L)]
vis = [False] * L
comp_id = [0] * L

for _ in range(m):
    u,v = map(int, input().split())
    u = xtoidx(u)
    v = xtoidx(v)
        
    adj[notx((u))].append(v)
    rev_adj[v].append(notx(u))
    adj[notx((v))].append(u)
    rev_adj[u].append(notx(v))
    

    

# 1
for i in range(L):
    if not vis[i]:
        dfs1(i)

# 2
vis = [False] * L
comps = 0
for i in range(len(order) - 1, -1, -1):
    v = order[i]
    if not vis[v]:
        comps += 1
        dfs2(v, comps)

# print(comps)
#print(*comp_id)

scc = [[] for _ in range(comps + 1)]
for i in range(1, n + 1):
    if comp_id[i] == comp_id[notx(i)]:
        print("OTL")
        exit()
    scc[comp_id[i]].append(i)
    scc[comp_id[notx(i)]].append(notx(i))

visit2 = [False] * L
ans = [0 for _ in range(n)]
for i in range(1, len(scc)):
    for val in scc[i]:
        if visit2[val]:
            continue
        visit2[val] = True
        visit2[notx(val)] = True
        
        if val > n:
            ans[notx(val) - 1] = 1
        else:
            ans[val - 1] = 0

print("^_^")