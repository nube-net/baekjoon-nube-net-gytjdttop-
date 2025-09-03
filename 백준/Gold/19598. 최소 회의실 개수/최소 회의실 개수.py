import sys
from heapq import heappop, heappush, heapify

n = int(sys.stdin.readline())
heap = []

for o in range(n):
    x, y = map(int, sys.stdin.readline().split())
    heap.append((x, y))
heapify(heap)

room_count = 0
room_ends = []

for i in range(n):
    start, end = heappop(heap)
    
    if room_ends and room_ends[0] <= start:
        heappop(room_ends)
    heappush(room_ends, end)
    
    room_count = max(room_count, len(room_ends))

print(room_count)
