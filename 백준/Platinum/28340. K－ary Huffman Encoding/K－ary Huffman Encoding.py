from heapq import heappush,heappop
import sys
input =sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    pq = []
    for i in a:
        heappush(pq, i)
    while (len(pq)-1)%(k-1):
        heappush(pq, 0)
    ans = 0
    while len(pq) > 1:
        tmp = 0
        for _ in range(min(k, len(pq))):
            tmp += heappop(pq)
        heappush(pq, tmp)
        ans += tmp
    print(ans)


