from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
indegree = [0] * n
q = deque()

for _ in range(m):
    S = list(map(int, input().split()))
    for i in range(1,len(S)-1):
        a, b = S[i], S[i+1]
        graph[a - 1].append(b - 1)
        indegree[b - 1] += 1

for i in range(n):
    if indegree[i] == 0:
        q.append(i)

order = []

while q:
    # print(q)
    # print(order)

    curr = q.popleft()
    order.append(curr)
    for next_node in graph[curr]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)


if len(order) != n:
    print("0")
else:
    for node in order:
        print(node + 1, end=' ')
    print()
