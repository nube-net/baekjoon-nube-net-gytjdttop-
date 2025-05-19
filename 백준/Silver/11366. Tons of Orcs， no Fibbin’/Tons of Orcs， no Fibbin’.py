import sys
input = sys.stdin.readline

def fib(b):
    a = [[1, 1], [1, 0]]
    tmp = [[1, 1], [1, 0]]
    while b > 0:
        if b % 2 == 1:
            Q = [[0, 0], [0, 0]]
            Q[0][0] = (tmp[0][0]*a[0][0] + tmp[0][1]*a[1][0])
            Q[0][1] = (tmp[0][0] * a[0][1] + tmp[0][1] * a[1][1])
            Q[1][0] = (tmp[1][0] * a[0][0] + tmp[1][1] * a[1][0])
            Q[1][1] = (tmp[1][0] * a[0][1] + tmp[1][1] * a[1][1])
            tmp = list(Q)
        Q = [[0, 0], [0, 0]]
        Q[0][0] = (a[0][0] * a[0][0] + a[0][1] * a[1][0])
        Q[0][1] = (a[0][0] * a[0][1] + a[0][1] * a[1][1])
        Q[1][0] = (a[1][0] * a[0][0] + a[1][1] * a[1][0])
        Q[1][1] = (a[1][0] * a[0][1] + a[1][1] * a[1][1])
        a = list(Q)
        b = b // 2
    return tmp[1][1]
while True:
    x,y,n = map(int, input().split())
    if x==0 and y==0 and n==0:
        break
    if x == 0 and y == 0:
        print(0)
        continue
    print(x*fib(n) + y*fib(n+1))