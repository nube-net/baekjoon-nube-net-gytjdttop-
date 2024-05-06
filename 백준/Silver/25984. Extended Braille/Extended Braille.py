import sys
input = sys.stdin.readline

S = set()
n = int(input())
for _ in range(n):
    m = int(input())
    tmp = []
    for __ in range(m):
        x,y = map(int, input().split())
        tmp.append([x,y])

    tmp.sort()
    cur = []
    dx,dy = tmp[0][0], tmp[0][1]
    for x,y in tmp:
        cur.append((x-dx, y-dy))
    cur2 = tuple(cur)

    if cur2 in S:
        continue
    else:
        S.add(cur2)
print(len(S))