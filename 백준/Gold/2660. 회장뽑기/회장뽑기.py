import sys
input = sys.stdin.readline

n = int(input())

dist = [[float('inf')] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    dist[x-1][y-1] = 1
    dist[y-1][x-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

scores = [max(dist[i]) for i in range(n)]
min_score = min(scores)
a = [i + 1 for i in range(n) if scores[i] == min_score]

print(min_score, len(a))
print(*a)