import sys
M, N = map(int, sys.stdin.readline().split())
count = 0
Map = set()  # 하나 이상 연결된 정점
graph = [set() for i in range(M+1)]  # 연결된 정점들
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].add(y)
    graph[y].add(x)
    Map.add(x)
    Map.add(y)
for o in range(1,M+1):
    if not (o in Map):
        count +=1
stack = []
while Map :
    if stack:
        key = True
        tmp = stack[-1]
        for k in graph[tmp]:
            if k in Map:
                stack.append(k)
                Map.remove(k)
                key = False
                break
        if key :
            stack.pop()
    else:
        stack.append(Map.pop())
        count += 1

print(count)
