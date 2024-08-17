import sys
input = sys.stdin.readline

n,k= map(int, input().split())
if n<= k:
    print(n)
else:
    q = n//k
    r =n%k
    if r == 0:
        print(k)
    else:
        print(n//(q+1))
