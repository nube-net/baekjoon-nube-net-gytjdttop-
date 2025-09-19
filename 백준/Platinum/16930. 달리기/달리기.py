import sys
from collections import deque
input = sys.stdin.readline

# AC받은후 빠른코드 굼금해서 질문한 gpt코드
n, m, k = map(int,input().split())
a = [list(input().rstrip()) for _ in range(n)]
s1, s2, d1, d2 = map(int,input().split())

INF = 10**9
dist = [[INF]*m for _ in range(n)]
dist[s1-1][s2-1] = 0

q = deque()
q.append((s1-1, s2-1))
D = [(1,0), (-1,0), (0,-1), (0,1)]

while q:
    x, y = q.popleft()
    for dx, dy in D:
        for step in range(1, k+1):
            nx, ny = x + dx*step, y + dy*step
            if not (0 <= nx < n and 0 <= ny < m): break
            if a[nx][ny] == "#": break
            if dist[nx][ny] < dist[x][y] + 1: break  # 이미 더 좋은 경로가 있음
            if dist[nx][ny] == dist[x][y] + 1: continue  # 같은 거리로 중복 방문 방지
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

print(-1 if dist[d1-1][d2-1] == INF else dist[d1-1][d2-1])
