import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n, L = map(int, input().split())
num = list(map(int, input().split()))
heap = []
ans = []

for i in range(n):
    while heap:
        if i - heap[0][1] >= L: 
            heappop(heap)
        else:
            break
    heappush(heap, (num[i], i))
    ans.append(heap[0][0])
print(*ans)
