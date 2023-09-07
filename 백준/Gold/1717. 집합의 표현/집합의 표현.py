import sys
input = sys.stdin.readline
def find(a):
    path = []
    while S[a] != a:
        path.append(a)
        a = S[a]
    for node in path: 
        S[node] = a
    return a

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a < root_b:
        S[root_b] = root_a
    else:
        S[root_a] = root_b

n, m = map(int, input().split())
S = [i for i in range(n + 1)]

for _ in range(m):
    x, a, b = map(int, input().split())
    if x:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)
