import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(a):
    for b in adj[a]:
        if visited[b]:
            continue
        visited[b] = True
        if match[b] == -1 or dfs(match[b]):
            match[b] = a
            return True
    return False

def bipartite_match(n_left, n_right):
    res = 0
    global visited
    for a in range(1, n_left + 1):
        visited = [False] * (n_right + 1)
        if dfs(a):
            res += 1
    return res

n_left, n_right = map(int, input().split())
adj = [[] for _ in range(n_left + 1)]
for a in range(1,n_left+1):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]+1):
        b = tmp[i]
        adj[a].append(b)
match = [-1] * (n_right + 1)
print(bipartite_match(n_left, n_right))
