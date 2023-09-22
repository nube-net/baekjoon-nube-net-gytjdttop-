import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()

ans = 0
cur = 0 # 현재 이어져 있는 선 개수

for _, x in lines:
    if cur <= x:
        ans += x-cur
        cur = x
    else:
        cur = x
print(ans)
