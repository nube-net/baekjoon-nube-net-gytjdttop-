import sys
from heapq import heapify,heappush,heappop

n = int(sys.stdin.readline())

num = []
heapify(num)
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        if num:
            tmp = heappop(num)
            print(tmp[1])
        else :
            print(0)
    else :
        if a <0:
            heappush(num, (-a,a))
        else:
            heappush(num, (a,a))