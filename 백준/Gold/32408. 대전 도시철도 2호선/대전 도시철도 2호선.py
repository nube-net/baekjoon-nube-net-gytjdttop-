import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visit = [False for _ in range(n+1)]
visit[1] = True
S=set()
prev = [ -1 for _ in range(n+1)]
####
while q:
    cur = q.popleft()
    for i in graph[cur]:
        if not visit[i]:
            prev[i] = cur
            if i == n:
                x = i
                while prev[x] != -1:
                    S.add(x)
                    x = prev[x]
                break
            visit[i] = True
            q.append(i)
            
    if S:
        break
#####
S.add(1)
#print(S)
tmp = []
Sum = 0
for i in range(1,n+1):
    if i in S:
        continue
    q = deque([i])
    S.add(i)
    d = 1
    while q:
        x = q.popleft()
        for y in graph[x]:
            if y in S:
                continue
            S.add(y)
            q.append(y)
            d += 1
    tmp.append(d)
    Sum += d
ans = 0
while tmp:
    x = tmp.pop()
    Sum -= x
    ans += x*Sum
    
print(ans)