import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
visit = [0 for _ in range(n)]
ans = 0

for i in range(n):
    if not visit[i]:
        path = []
        cur = i
        while not visit[cur]:
            visit[cur] = 1
            path.append(cur)
            cur = a[cur] - 1
        if cur in path:
            idx = path.index(cur)
            cycle_len = len(path) - idx
            ans += cycle_len

print(ans)
