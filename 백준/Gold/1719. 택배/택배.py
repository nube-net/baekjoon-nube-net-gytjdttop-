import sys
inputF = sys.stdin.readline

V, E = map(int, inputF().split())

cost = [[float('inf')]*V for _ in range(V)]  # 가중치
S = [[[i+1] for i in range(V)]for _ in range(V)]  # 경로 저장,

for i in range(V):
    cost[i][i] = 0

for _ in range(E):
    x, y, c = map(int, inputF().split())
    cost[x-1][y-1] = min(cost[x-1][y-1], c)
    cost[y- 1][x - 1] = min(cost[y - 1][x - 1], c)

for i in range(V):  # 거쳐 가는 노드
    for j in range(V):  # 출발 노드
        for k in range(V):  # 도착 노드
            if cost[j][k] > cost[j][i] + cost[i][k]:
                cost[j][k] = cost[j][i] + cost[i][k]
                S[j][k] = S[j][i] + S[i][k]

for i in range(V):
    for j in range(V):
        if cost[i][j] == float('inf'):
            cost[i][j] = 0


for i in range(V):
    for j in range(V):
        if i == j:
            print('-', end=' ')
        else:
            print(S[i][j][0], end=' ')
    print()

