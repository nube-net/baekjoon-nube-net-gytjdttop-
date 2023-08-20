import sys
inputF = sys.stdin.readline

n = int(inputF())
tasks = [tuple(map(int, inputF().split())) for _ in range(n)]

tasks.sort(key=lambda x: x[1])

deadline = 0
time = 0
result =  1000001
k = False
for x, y in tasks:
    deadline = y
    time += x
    result = min(deadline - time, result)
    if time > deadline:
        k = True
        break

if k:
    print(-1)
else:
    print(result)
