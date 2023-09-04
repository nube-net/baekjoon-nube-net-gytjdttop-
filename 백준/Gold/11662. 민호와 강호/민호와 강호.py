ax, ay, bx, by, cx, cy, dx, dy = map(float, input().split())
ans = float('inf')
for _ in range(10000):
    # 3분의 1 지점
    mxa = ax + (bx - ax) / 3
    mya = ay + (by - ay) / 3
    mxc = cx + (dx - cx) / 3
    myc = cy + (dy - cy) / 3
    # 3분의 2 지점
    mxb = ax + 2 * (bx - ax) / 3
    myb = ay + 2 * (by - ay) / 3
    mxd = cx + 2 * (dx - cx) / 3
    myd = cy + 2 * (dy - cy) / 3

    # 삼분 탐색
    left = ((mxc-mxa)**2 + (myc-mya)**2)**0.5
    right = ((mxd-mxb)**2 + (myd-myb)**2)**0.5
    ans = min(ans, left, right)
    if left > right:
        ax = mxa
        ay = mya
        cx = mxc
        cy = myc
    elif left < right:
        bx = mxb
        by = myb
        dx = mxd
        dy = myd
    else:
        ax = mxa
        ay = mya
        cx = mxc
        cy = myc
        bx = mxb
        by = myb
        dx = mxd
        dy = myd

print(ans)