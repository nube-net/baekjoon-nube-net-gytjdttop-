import sys
from heapq import  heappop,heappush,heapify
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
hq = []
dp = [[i-1, i+1] for i in range(n+1)]
dp[0][0] = 0
dp[n][1] = n
dist = [sys.maxsize for _ in range(n+1)]
visited = [True for _ in range(n+1)]
for i in range(1,n):
    dist[i] = arr[i]-arr[i-1]
    heappush(hq,[dist[i],i])
ans=0
while k > 0:
    val, idx = heappop(hq)
    if visited[idx]:
        k -= 1
        ans += val

        l = dp[idx][0]
        r = dp[idx][1]
        dist[idx] = dist[l] +dist[r] - dist[idx]
        heappush(hq, [dist[idx],idx])

        visited[l] = False
        visited[r] = False
        L = dp[l][0]
        R = dp[r][1]
        dp[L][1] = idx
        dp[R][0] = idx
        dp[idx][0] = L
        dp[idx][1] = R
print(ans)
