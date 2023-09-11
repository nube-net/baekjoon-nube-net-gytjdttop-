import sys
inputF = sys.stdin.readline

V, E = map(int, inputF().split())

cost = [[float('inf')]*V for _ in range(V)]  # 가중치
for i in range(V):
    cost[i][i] = 0

for _ in range(E):
    x, y, c = map(int, inputF().split())
    cost[x-1][y-1] = min(cost[x-1][y-1], c)

for i in range(V):  # 거쳐 가는 노드
    for j in range(V):  # 출발 노드
        for k in range(V):  # 도착 노드
            cost[j][k] = min(cost[j][k], cost[j][i] + cost[i][k])
'''
for i in range(V):
    for j in range(V):
        if cost[i][j] == float('inf'):
            cost[i][j] = 0
            '''
ans = float('inf')
for i in range(V):  #  출발
    for j in range(V):  # 도착
        if i == j:
            continue

        ans = min(ans, cost[i][j] + cost[j][i])
if ans == float('inf'):
    print(-1)
else:
    print(ans)

