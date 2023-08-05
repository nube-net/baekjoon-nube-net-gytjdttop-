import sys
inputF = sys.stdin.readline
INF = int(1e10)

def bf():  # 밸만 포드
    dist = [0] * (n+1)

    for i in range(n):
        for j in range(len(edges)):
            cur, next_node, cost = edges[j]
            if dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                if i == n - 1:  
                    return True
    return False

T = int(inputF())
for q in range(T):        
    n, m, w = map(int, inputF().strip().split())
    edges = []

    for _ in range(m):
        a, b, c = map(int, inputF().strip().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(w):
        a, b, c = map(int, inputF().strip().split())
        edges.append((a, b, -c))

    if bf():
        print('YES')
    else:
        print('NO')
