import sys
input = sys.stdin.readline

n =int(input())
a = list(map(int, input().split()))
l, h = min(a) - n, max(a) + n

ans = sys.maxsize
for _ in range(100):
    lm = l+(h-l)//3
    hm = h-(h-l)//3
    
    val_l, val_h = 0, 0
    for i in range(n):
        val_l += abs(lm+i - a[i])
        val_h += abs(hm+i - a[i])
        
    if val_l <= val_h:
        ans = min(ans, val_l)
        h = hm
    else:
        ans = min(ans, val_h)
        l = lm
print(ans)