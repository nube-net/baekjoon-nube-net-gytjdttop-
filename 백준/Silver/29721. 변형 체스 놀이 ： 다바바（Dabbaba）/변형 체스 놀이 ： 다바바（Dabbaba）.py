import sys

n, m = map(int, sys.stdin.readline().split())

visited = set()
dx = [2, -2, 0, 0]
dy = [0, 0, -2, 2]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    visited.add((x, y))

    for i in range(4):
        X, Y = x + dx[i], y + dy[i]

        if X < 0 or Y < 0 or X >= n or Y >= n or (X, Y) in visited:
            continue

        visited.add((X, Y))

ans = len(visited)-m
print(ans)
