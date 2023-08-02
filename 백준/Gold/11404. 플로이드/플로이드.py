import sys
inputF = sys.stdin.readline

n = int(inputF())
bus = int(inputF())

cost = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0

for _ in range(bus):  # 버스 정보 입력
    x, y, c = map(int, inputF().split())
    cost[x-1][y-1] = min(cost[x-1][y-1], c)

for i in range(n):  # 거쳐 가는 도시
    for j in range(n):  # 출발 도시
        for k in range(n):  # 도착 도시
            cost[j][k] = min(cost[j][k], cost[j][i] + cost[i][k])

for i in range(n):
    for j in range(n):
        if cost[i][j] == float('inf'):
            cost[i][j] = 0

for i in cost:
    print(*i)
