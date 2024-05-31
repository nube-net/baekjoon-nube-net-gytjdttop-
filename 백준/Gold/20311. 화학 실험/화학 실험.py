import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline


n, k = map(int, input().split())
arr = list(map(int, input().split()))
hq = []
for i in range(k):
    d = arr[i]
    heappush(hq, [-d,i+1])
pre, pre_idx = heappop(hq)
ans=[pre_idx]
pre += 1
while hq:
    cur, cur_idx = heappop(hq)
    ans.append(cur_idx)
    cur += 1

    if pre < 0:
        heappush(hq, [pre,pre_idx])
    pre = cur
    pre_idx = cur_idx

if pre <0 or hq:
    print(-1)
else:
    print(*ans)