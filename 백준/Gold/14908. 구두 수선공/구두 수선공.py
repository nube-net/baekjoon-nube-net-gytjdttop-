import sys

N = int(sys.stdin.readline())

Task = []
for k in range(N):
    x, y = map(int, sys.stdin.readline().split())
    Task. append([x, y, k+1])
Task.sort( key=lambda x: ( x[0]/x[1], x[1],x[2]) )
order = []
end=0
tmp=[]
key = False
for o in range(len(Task)-1):
    if Task[o][0]/ Task[o][1]== Task[o+1][0]/Task[o+1][1]:
        if not key:
            start = o
            key =True
        end = o+1
    else:
        if end !=0:
            tmp=Task[start:end+1].copy()
            tmp.sort(key=lambda x: (x[0] / x[1],  x[2]))
            Task[start:end + 1] = tmp.copy()
            key = False
if end !=0:
    tmp=Task[start:end+1].copy()
    tmp.sort(key=lambda x: (x[0] / x[1],  x[2]))
    Task[start:end + 1] = tmp.copy()

for i in Task:
    order.append(i[2])
print(*order)