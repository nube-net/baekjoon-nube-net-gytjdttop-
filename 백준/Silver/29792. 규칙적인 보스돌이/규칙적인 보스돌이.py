import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
damage = [int(input()) for _ in range(n)]
Boss = [list(map(int, input().split())) for _ in range(k)]
damage.sort(reverse=True)

ans0 = 0
for i in range(m):
    c = damage[i]
    Q = deque()
    Q.append((900, 0))

    for hp, coin in Boss:
        l = len(Q)
        for _ in range(l):
            x, y = Q.popleft()
            Q.append((x, y))
            time = hp// c
            if hp%c > 0:
                time += 1

            if x-time >= 0:
                Q.append((x-time, y+coin))
    ans = 0
    while Q:
        x,y = Q.popleft()
        ans = max(ans, y)

    ans0 += ans
print(ans0)



