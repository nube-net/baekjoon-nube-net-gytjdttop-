import sys
inputF = sys.stdin.readline

V = int(inputF())
E = int(inputF())

cost = [[float('inf')]*V for _ in range(V)]  # 가중치
S = [[[i+1] for i in range(V)]for _ in range(V)]  # 경로 저장,

for i in range(V):
    cost[i][i] = 0

for _ in range(E):
    x, y, c = map(int, inputF().split())
    cost[x-1][y-1] = min(cost[x-1][y-1], c)

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

for i in cost:
    print(*i)

for i in range(V):
    for j in range(V):
        if cost[i][j] == 0:
            print(0)
            continue
        print(len(S[i][j])+1,i+1,*[x for x in S[i][j]])


