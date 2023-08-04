import sys
import heapq

n = int(sys.stdin.readline().rstrip())
num = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
result = 0

heapq.heapify(num)

while len(num) > 1:
    a = heapq.heappop(num)
    b = heapq.heappop(num)
    result += a + b
    heapq.heappush(num, a + b)

print(result)