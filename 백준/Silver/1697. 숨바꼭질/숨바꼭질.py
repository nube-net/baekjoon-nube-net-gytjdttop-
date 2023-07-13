import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
c=0
check ={N}
Map= set()
tmp =set()
while True :
    if K in check:
        break
    c+=1
    tmp=set()
    for i in check:
        if i < 0 :
            continue
        elif i >100000 :
            continue
        if i in Map:
            continue
        else:
            Map.add(i)
            if not (i-1 in Map):
                tmp.add(i-1)
            if not (i+1 in Map):
                tmp.add(i+1)
            if not (i*2 in Map):
                tmp.add(i*2)
    check = set()
    check.update(tmp)

print(c)