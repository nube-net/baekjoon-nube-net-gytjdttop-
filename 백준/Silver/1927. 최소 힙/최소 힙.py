import sys
from heapq import heappush, heappop, heapify
heap =[]
heap1 = heap
heapify(heap)
result=[]
n= int(sys.stdin.readline())

for i in range(n):
    a= int(sys.stdin.readline())
    if a ==0 :
        if heap ==[]:
            result.append(0)
        else:
            result.append(heappop(heap))
    else :
        heappush(heap,a)

for k in result:
    print(k)