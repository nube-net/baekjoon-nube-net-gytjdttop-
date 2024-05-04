import sys
input = sys.stdin.readline
# 볼록껍질 공부중
def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (x3 - x1)*(y2 - y1) > 0

def convex_hull(positions):
    # Graham Scan
    convex = []
    for p in positions:
        while len(convex) >= 2 and not ccw(convex[-2], convex[-1], p):
            convex.pop()
        convex.append(p)
    return len(convex)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
ans = convex_hull(arr) + convex_hull(arr[::-1]) - 2
print(ans)
