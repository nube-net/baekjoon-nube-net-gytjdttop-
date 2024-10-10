import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
cnt = 0
d = 0
pre = a[0]
f = True
for i in range(1, n):
    cur = a[i]
    if f:
        if pre > cur:
            cnt += 1
            f = False
    else:
        if pre < cur:
            cnt+=1
            f = True
    pre = cur
if cnt:
    d += int(bool((cnt+1)//2))
cnt //= 2
cnt += d
ans = 0
while cnt > 1:
    cnt = cnt//2 + cnt%2
    ans += 1
print(ans+cnt)