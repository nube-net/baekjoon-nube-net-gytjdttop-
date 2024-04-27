import sys
from heapq import heappop,heappush, heapify
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
a = deque(map(int,input().split()))
hq = []
heapify(hq)
ans = 0
t = 0

for _ in range(k):
    heappush(hq, a.popleft())
    if not a:
        break

while hq:
    cur = heappop(hq)
    ans = max(ans, cur - t)
    t = cur
    if a:
        tmp = a.popleft()
        heappush(hq, t+tmp)

print(ans)