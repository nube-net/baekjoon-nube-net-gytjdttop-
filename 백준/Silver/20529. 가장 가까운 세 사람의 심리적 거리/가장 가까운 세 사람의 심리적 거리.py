import sys
from itertools import combinations
inputF = sys.stdin.readline

T = int(inputF())

for _ in range(T):
    n = int(inputF())
    s = list(map(str, inputF().rstrip().split()))
    if n > 32:
        print(0)
        continue

    cnt = float('inf')
    for x, y, z in list(combinations(s, 3)):
        c = 0
        for i in range(4):
            if x[i] != y[i]:
                c += 1
            if x[i] != z[i]:
                c += 1
            if z[i] != y[i]:
                c += 1
        cnt = min(cnt, c)
    print(cnt)