import sys
import heapq

inputF = sys.stdin.readline

n = int(inputF())
a = [int(inputF()) for _ in range(n)]

heapq.heapify(a) 

while a:
    tmp = heapq.heappop(a) 
    print(tmp)
