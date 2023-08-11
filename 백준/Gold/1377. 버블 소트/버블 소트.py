import sys
from heapq import  heappop, heappush, heapify
inputF = sys.stdin.readline

n = int(inputF())
num = [(int(inputF()), _) for _ in range(1, n+1)]
heapify(num)

result = 0
for i in range(n):
    _, x = heappop(num)
    result = max(result, x-i)

print(result)
