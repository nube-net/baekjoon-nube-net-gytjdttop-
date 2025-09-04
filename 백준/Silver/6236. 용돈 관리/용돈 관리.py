import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a =[int(input()) for _ in range(n)]

l, h = max(a), n*10000 + 1
ans = sys.maxsize
while l<h:
    x = (l+h)//2
    
    cur = int(x)
    cnt = 1
    for i in a:
        if i <= cur:
            cur -= i
        else:
            cur = x-i
            cnt += 1
        if cnt > m:
            break
    if cnt <= m:
        ans = min(ans, x)
        h = x
    else:
        l = x+1
    
print(ans)
            