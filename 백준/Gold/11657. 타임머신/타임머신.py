# 1865 웜홀 문제 풀기 전 밸만포드 공부용 
import sys
inputF = sys.stdin.readline
INF = int(1e10)

def bf(start):
    dist[start] = 0

    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == n-1:
                    return True
    return False


n, m = map(int, inputF().split())

edges =[]
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, inputF().split())

    edges.append((a,b,c))

cycle = bf(1)

if cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])