import sys
input =sys.stdin.readline

def cal(t):
    min_x, min_y = 1e7, 1e7
    max_x, max_y = -1e7, -1e7
    for px, py, vx, vy in loc:
        min_x = min(min_x, px + vx * t)
        max_x = max(max_x, px + vx * t)
        min_y = min(min_y, py + vy * t)
        max_y = max(max_y, py + vy * t)

    return max(max_y-min_y,max_x-min_x)

n = int(input())
loc = [list(map(int,input().split())) for _ in range(n)]

left, right = 0, 2000001
ans = 100000001
for _ in range(1000):
    mid_l = left + (right-left)/3
    mid_r = left + (right - left)*2 / 3
    L,R= cal(mid_l),cal(mid_r)
    if L <= R:
        right = mid_r
        ans = min(ans,R)
    else:
        left = mid_l
        ans = min(ans,L)
print(ans)

