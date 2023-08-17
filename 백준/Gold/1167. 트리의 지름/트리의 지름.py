import sys
inputF = sys.stdin.readline
# 루트는 어디든 상관 없다
n = int(inputF())
tree = [[] for _ in range(n+1)]

# 바뀐 부분
for _ in range(n):
    line = list(map(int, inputF().split()))
    if len(line) == 2:
        continue
    for i in range(1, len(line)-1, 2):
        x, y = line[i:i+2]
        tree[x].append((line[0], y))
        tree[line[0]].append((x, y))


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
