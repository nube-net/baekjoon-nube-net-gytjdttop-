import sys

input = sys.stdin.readline

n,m = map(int,input().split())
x = []
y = []
for _ in range(m):
    i,j = map(int,input().split())
    x.append(i)
    y.append(j)
x.sort()
y.sort()
ans = 0
for i in range(m):
    ans += abs(x[i]-x[m//2]) + abs(y[i]-y[m//2])
print(ans)