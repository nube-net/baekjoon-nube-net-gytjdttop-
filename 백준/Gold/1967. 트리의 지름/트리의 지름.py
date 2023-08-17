import sys
inputF = sys.stdin.readline

n = int(inputF())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y, z = map(int, inputF().split())
    tree[x].append((y, z))
    tree[y].append((x, z))

stack = [(1,0)]
visited = set()
D = 0
start = 0
while stack:
    x, d = stack.pop()
    if x in visited:
        continue
    visited.add(x)

    if d >= D:
        D = d
        start = x

    for y, z in tree[x]:
        stack.append((y, d+z))

stack = [(start, 0)]
visited = set()
D = 0
while stack:
    x, d = stack.pop()
    if x in visited:
        continue
    visited.add(x)

    D = max(D, d)

    for y, z in tree[x]:
        stack.append((y, d + z))
print(D)


