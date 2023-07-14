import sys

def code(n,r,c):
    a=r
    b=c
    if r <= 2**(n-1):
        if c > 2**(n-1):
            result[0] += (2**(n-1))**2
            b-= 2**(n-1)
    else:
        if c <= 2**(n-1):
            result[0] += ((2**(n-1))**2)*2
            a -= 2 ** (n - 1)
        else:
            result[0] += ((2 ** (n - 1)) ** 2) * 3
            a -= 2 ** (n - 1)
            b -= 2 ** (n - 1)

    if n==1:
        return
    else:
        code(n-1, a, b)

result =[0]
n, r, c = map(int, sys.stdin.readline().split())

code(n,r+1,c+1)
print(*result)