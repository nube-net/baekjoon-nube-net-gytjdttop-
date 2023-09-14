import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
key = True
b = sorted(a)
while key:
    key = False
    for i in range(n-2):
        if a[i] > a[i+2]:
            a[i], a[i+2] = a[i+2], a[i]
            key = True


if a == b:
    print('YES')
else:
    print('NO')