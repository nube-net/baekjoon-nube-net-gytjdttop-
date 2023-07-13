import sys
from collections import deque
inputF = sys.stdin.readline

def DFS(start) :
    while graph[start]:
        i= min(graph[start])
        graph[start].remove(i)
        if i in Map:
            continue
        else:
            Map.add(i)
            result1.append(i)
            DFS(i)


Q = deque()
result1 = []
result2 = []

n, m, v = map(int, inputF().split())

Map, Map2 = set(), set()  # 방문 노드 저장
graph = [set() for _ in range(n+1)]  # 연결 노드
graph2 = [set() for _ in range(n+1)]
for i in range(m):
    x,y = map(int, inputF().split())
    if not x in graph[y]:
        graph[y].add(x)
        graph2[y].add(x)
    if not y in graph[x]:
        graph[x].add(y)
        graph2[x].add(y)

# DFS
Map.add(v)
result1.append(v)
DFS(v)
print(*result1)

# BFS
Q.append(v)
Map2.add(v)
while Q :
    tmp = Q.popleft()
    result2.append(tmp)
    while graph2[tmp]:
        tmp1 = min(graph2[tmp])
        graph2[tmp].remove(tmp1)
        if not (tmp1 in Map2):
            Q.append(tmp1)
            Map2.add(tmp1)
print(*result2)