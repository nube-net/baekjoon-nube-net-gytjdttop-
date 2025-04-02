import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]
x = 1
for i in range(1,m):
    a[0][i] =a[0][i-1] + x
    if x >0 :
        x +=1
    else:
        x -=1
    x *= -1
x = abs(x)
for i in range(1,n):
    for j in range(m):
        a[i][j] = a[i-1][j] + x

        if x > 0:
            x += 1
        else:
            x -= 1
        x *= -1
    if x> 0:
        x += m-1
    else:
        x -= m-1
    if not m%2:
        x *= -1
tmp = sys.maxsize
for k in a:
    tmp = min(tmp, min(k))
tmp = abs(tmp)
for i in range(n):
    for j in range(m):
        a[i][j] += tmp+1
for k in a:
    print(*k)

"""0 1 -1 2 -2 (m-1)
5 -5 6 -6 7"""