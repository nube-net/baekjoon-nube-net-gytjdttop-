import sys
from heapq import heapify,heappop,heappush
input = sys.stdin.readline

n = int(input())
color = list(input())
weight = list(map(int, input().split()))

if n<=2:
    print(0)
    exit()
### 연속된 같은 색 제거 과정 넣기 ###

ans = 0
#color.append("o")
#weight.append(0)
S =set()
hq0 = []
hq = []
cur_ = color[0]
cnt = 1
for i in range(n):
    if cur_ == color[i]:
        S.add(i)
        heappush(hq0, (-weight[i], i))
    else:
        cur_ = color[i]
        if (0 in S) or (n-1 in S):
            S = set()
            S.add(i)
            hq0 = []
            heappush(hq0, (-weight[i], i))
            continue
        w, idx = heappop(hq0)
        heappush(hq, -weight[idx])  # weigh, color, index
        hq0 = []
        S = set()
        cnt += 1
        S.add(i)
        heappush(hq0, (-weight[i], i))
l = len(hq)//2 + len(hq)%2
for _ in range(l):
    ans += heappop(hq)
print(-ans)

