import sys

T = int(sys.stdin.readline())

for _ in range(T):
    m, n, x, y = map(int, sys.stdin.readline().split())  # k번째 해 -> k%(m,n) 만약 0이면 1

    key = False
    k = x
    tmp = y
    while k <= m*n:

        for i in range(tmp,k*n+1,n):
            if k == i:
                key = True
                break
            elif k < i:
                tmp = i
                break
        if key:
            break
        k += m

    if key:
        print(k)
    else:
        print(-1)

