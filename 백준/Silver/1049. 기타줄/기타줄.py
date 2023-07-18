import sys

n, m = map(int, sys.stdin.readline().split())
result=0
a = []
x, y = 1000, 1000
for _ in range(m):
    nx, ny = map(int, sys.stdin.readline().split())
    x = min(x, nx)
    y = min(y, ny)

x = min(x, 6*y)
result += x*(n//6)
result += min(x, y*(n%6))


print(result)
