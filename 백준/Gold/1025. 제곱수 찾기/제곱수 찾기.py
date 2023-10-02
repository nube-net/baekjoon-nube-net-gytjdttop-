import sys
import math
input = sys.stdin.readline

n, m = map(int,input().split())
Map = [list(input().strip()) for _ in range(n)]
ans = -1

for i in range(n):
    for j in range(m):
        for r in range(-n, n):
            for c in range(-m, m):
                if not r and not c:
                    continue

                tmp = ""
                x, y = i, j
                while (0 <= x < n) and (0 <= y < m):
                    tmp += Map[x][y]

                    if int(math.sqrt(int(tmp)))**2 == int(tmp):
                        ans = max(int(tmp), ans)
                    x += r
                    y += c
print(ans)