import sys
import heapq
inputF = sys.stdin.readline

n = int(inputF())
tmp=[]
data = []
result=[]
for i in range(n):
    result.append(0)
    tmp.append([0,i])
    x,y = map(int, inputF().split())
    data.append((x,y,i))

heapq.heapify(data)
for o in range(n):
    a = heapq.heappop(data)
    for k in data:
        if a[1]<k[1]:
            if a[0] != k[0] :
                tmp[a[2]][0] +=1
heapq.heapify(tmp)

tmp0=0
order = 1
c=[]
for o in range(n):
    b = heapq.heappop(tmp)
    result[b[1]] = b[0]+1



print(*result)