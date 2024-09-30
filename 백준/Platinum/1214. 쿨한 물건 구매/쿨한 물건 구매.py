import sys
input = sys.stdin.readline

d, p, q = map(int,input().split())
if p == q:
    print((d//p)*p + bool(d%p)*p)
else:
    if p < q:
        tmp = p
        p = q
        q = tmp
    # p > q
    ans = (d//p)*p + bool(d%p)*p
    for i in range(min(d//p+1,q+1)):
        if d < i*p:
            break
        tmp = d-i*p
        k = i*p+(tmp//q)*q + bool(tmp%q)*q
        #print(i,k)
        ans = min(ans, k)
    print(ans)
