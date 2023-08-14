import sys
inputF = sys.stdin.readline

n = int(inputF())
graph = [set() for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, inputF().split())
    graph[x].add(y)
    graph[y].add(x)

Q = set()
Q.add(1)

while Q:
    tmp = set()
    while Q:
        a = Q.pop()
        for k in graph[a]:
            if parent[k] == 0:
                parent[k] = a
                tmp.add(k)
    Q = set(tmp)

for i in parent[2:]:
    print(i)
