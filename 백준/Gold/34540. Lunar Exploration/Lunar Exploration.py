import sys
input = sys.stdin.readline

n = int(input())
robot = [list(map(int, input().split())) for _ in range(n)]
x, y, d = input().split()
x = int(x)
y = int(y)

if d == "E":
    axis = 1
    st = x
    axis_val = y
else:
    axis = 0
    st = y
    axis_val = x

ans = 0
a = []
for i in range(n):
    ans += abs(axis_val - robot[i][axis])
    a.append(robot[i][(axis + 1) % 2])

a.sort()
for i in range(n):
    ans += abs(st + i - a[i])

print(ans)
