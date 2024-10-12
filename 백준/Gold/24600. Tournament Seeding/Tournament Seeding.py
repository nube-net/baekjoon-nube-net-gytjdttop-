import sys
input = sys.stdin.readline

n,k= map(int,input().split())
a = [int(input()) for _ in range(2**n)]
a.sort()
tmp = list(a)
small = a[:2**(n-1)]
big = a[2**(n-1):]
ans =0
for _ in range(n):
    small = tmp[:2 ** (n - 1)]
    big = tmp[2 ** (n - 1):]
    l,h = 2**(n-1)-1, 2**(n-1)-1
    while l>=0 and h>=0:
        if big[h]-small[l]<=k:
            ans +=1
            h-=1
            l-=1
        else:
            h-=1
    n -= 1
    tmp = list(big)
print(ans)