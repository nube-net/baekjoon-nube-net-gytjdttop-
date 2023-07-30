import sys
inputF = sys.stdin.readline

# 입력 및 초기 설정
n, m = map(int, inputF().split())

graph = [[0]*n for _ in range(n)]  # 경로 생성, 디폴트 값 false(=0)
for _ in range(m):  # 경로 있으면 true(=1)
    x, y = map(int, inputF().split())
    graph[x-1][y-1] = 1
    graph[y-1][x-1] = 1

# DP(플로이드-워셜)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            elif  graph[j][i] and  graph[i][k]:
                if graph[j][k] == 0:
                    graph[j][k] = graph[j][i] + graph[i][k]
                else:
                    graph[j][k] = min(graph[j][k] , graph[j][i] + graph[i][k])
tmp = 25000

for i in range(n):
    if sum(graph[i]) <tmp:
        tmp = sum(graph[i])
        result = i+1
print(result )
