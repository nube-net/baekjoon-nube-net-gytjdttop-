import math
import sys
input = sys.stdin.readline

n, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

d1 = a[0]
for i in a:
    d1 = math.gcd(d1, i)
for i in range(n):
    a[i] = a[i]//d1

d2 = b[0]
for i in b:
    d2 = math.gcd(d2, i)
for i in range(n):
    b[i] = b[i]//d2

tmp = 1
for i in range(n):
    if b[i]>0:
        tmp = max(tmp, (a[i] - 1) // b[i] + 1)

print((10 ** (p + 2)) // d1, (10 ** (p + 2)) // d2 * tmp)
