k, n = map(int, input().split())
if n == 1:
    print(-1)
else:
    a = (k*n)//(n-1)
    if(k*n)%(n-1) != 0:
        a += 1 
    print(a)