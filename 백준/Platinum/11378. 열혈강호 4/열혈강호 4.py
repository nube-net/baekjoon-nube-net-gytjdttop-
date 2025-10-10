import sys
input = sys.stdin.readline

def dfs(a):
    for b in adj[a]:
        if visited[b] == cnt:
            continue
        visited[b] = cnt
        if match[b] == -1 or dfs(match[b]):
            match[b] = a
            return True
    return False

n, m, k = map(int, input().split())
adj = [[] for _ in range(n+1)]
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    adj[i] = tmp[1:]

match = [-1 for _ in range(m+1)]  # 매칭 여부
ans = 0
cnt = 0
visited = [0 for _ in range(m+1)]
for a in range(1, n+1):
    cnt += 1
    if dfs(a):
        ans += 1
cnt +=1

for a in range(1, n+1):
    if k == 0:
        break
    while dfs(a) and k > 0:
        ans +=1
        cnt +=1
        k-=1

print(ans)
