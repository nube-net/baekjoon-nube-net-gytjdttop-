import sys


n = int( sys.stdin.readline() )

memory= {n}
c= 0

while not (1 in memory):
    c+=1
    tmp= set()
    for k in memory:
        if k%3 == 0:
            tmp.add(k//3)
        if k%2 == 0:
            tmp.add(k//2)
        tmp.add(k-1)
        memory = set()
        memory.update(tmp)

print(c)



