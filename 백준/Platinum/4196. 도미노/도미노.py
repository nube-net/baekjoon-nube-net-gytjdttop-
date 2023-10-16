import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited.add(v)
    for i in graph[v]:
        if i not in visited:
            dfs(graph, i, visited)
    stack.append(v)

def dfs2(graph2, v, visited):
    visited.add(v)
    tmp.add(v)
    for i in graph2[v]:
        if i not in visited:
            dfs2(graph2, i, visited)


T = int(input())
for __ in range(T):
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

    scc = []
    visited = set()
    while stack:
        k = stack.pop()
        if k in visited:
            continue
        tmp = set()
        dfs2(graph2, k, visited)
        scc.append(sorted(tmp))

    ans = []
    for i in scc:
        cnt = 0
        for j in i:
            for k in graph2[j]:
                if k in i:
                    continue
                cnt += 1
        if cnt == 0:
            ans.append(i)

    print(len(ans))