import sys
import heapq
inputF = sys.stdin.readline

n = int(inputF())

order = set()
for k in range(n):
    order.add(k+1)

report = []
for i in range(n):
    x,y = map(int, inputF().split())
    report.append((-y,x))
heapq.heapify(report)

result = 0
for o in range(n):
    tmp = heapq.heappop(report)
    for j in range(tmp[1],0,-1):
        if j in order :
            order.remove(j)
            result -= tmp[0]
            break

print(result)



