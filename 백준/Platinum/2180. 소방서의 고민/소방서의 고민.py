import sys

n = int(sys.stdin.readline())
a = []
t1 = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x == 0:
        t1 += y
    else:
        a.append((x, y))

a.sort(key = lambda x: x[1]/x[0])

result = 0
for x in a:
    t = result*x[0]+x[1]
    result += t
    result %= 40000

result += t1
result %= 40000

print(result)
