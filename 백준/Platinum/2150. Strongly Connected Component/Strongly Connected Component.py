import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited.add(v)
    for i in graph[v]:
        if i not in visited:
            dfs(graph, i, visited)
    stack.append(v)

def dfs2(graph2, v, visited):
    visited.add(v)
    tmp.append(v)
    for i in graph2[v]:
        if i not in visited:
            dfs2(graph2, i, visited)


V, E = map(int, input().split())

graph = [[] for _ in range(V+1)]
graph2 = [[] for _ in range(V+1)]
stack = []
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph2[b].append(a)
visited = set()
for k in range(1,V+1):
    if k not in visited:
        dfs(graph, k, visited)
# print(stack)

ans = []
visited = set()
while stack:
    k = stack.pop()
    if k in visited:
        continue
    tmp = []
    dfs2(graph2, k, visited)
    ans.append(sorted(tmp))
print(len(ans))
for i in sorted(ans):
    print(*i,-1)