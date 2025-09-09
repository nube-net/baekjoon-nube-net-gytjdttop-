import sys

input = sys.stdin.readline

n = int(input())
a = [0]+list(map(int,input().split()))
q = int(input())
cur = sum(a)
print(cur)
check = [0 for _ in range(n+1)]
for _ in range(q):
    tmp = list(map(int,input().split()))
    if tmp[0] == 1:
        dx = tmp[2]-a[tmp[1]]
        if not check[tmp[1]]:
            cur += dx
        a[tmp[1]] = tmp[2]
    else:
        if check[tmp[1]]:
            cur += a[tmp[1]]
            check[tmp[1]] = 0
        else:
            cur -= a[tmp[1]]
            check[tmp[1]] = 1
    print(cur)