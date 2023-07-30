import sys
from heapq import heappop, heappush, heapify

n = int(sys.stdin.readline())
a = []
for i in range(n):
    z, x, y = map(int, sys.stdin.readline().split())
    heappush(a, (x, y))  # 시작시각, 종료시각

b = [] 
tmp = heappop(a)[1]
heappush(b, tmp)

while a:
    x, tmp = heappop(a)
    if b[0] <= x:
        heappop(b)
    heappush(b, tmp)

print(len(b))
