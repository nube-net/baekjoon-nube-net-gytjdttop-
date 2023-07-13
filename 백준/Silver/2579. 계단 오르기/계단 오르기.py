import sys

n = int(sys.stdin.readline())

stairs = [int(sys.stdin.readline()) for _ in range(n)]


result = 0
tmp=set()
memory = {(1, stairs.pop())}  # (연속 횟수, 점수 총합)

while stairs:
    tmp3 = set()
    tmp1 = set()
    tmp2 = set()
    a = stairs.pop()
    while memory:
        b = memory.pop()
        if b[0] == 1:
            tmp2.add((2, b[1] + a))
            tmp3.add((3, b[1]))
        elif b[0] == 2:
            tmp3.add((3, b[1]))
        elif b[0] == 3:
            tmp1.add((1, b[1] + a))
    if tmp1:
        memory.add(max(tmp1))
    if tmp2:
        memory.add(max(tmp2))
    if tmp3:
        memory.add(max(tmp3))
for k in memory:
    result = max(result,k[1])
print(result)