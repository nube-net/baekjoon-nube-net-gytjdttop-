import sys
from collections import  deque
from heapq import heappop, heappush
input = sys.stdin.readline

n, k = map(int, input().split())
a = deque(map(int, input().split()))
hq = []
while a:
    cur = a.popleft()
    heappush(hq, cur)
    if len(hq) > k:
        print(heappop(hq), end =" ")
while hq:
    print(heappop(hq), end=" ")