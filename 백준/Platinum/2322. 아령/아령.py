import sys
input = sys.stdin.readline


n = int(input())
a = list(map(int, input().split()))
b = enumerate(a)
b = sorted(b, key = lambda x: x[1])
cnt = 0  # 교환 횟수
check = set()
ans = 0
k = False
if b[0][0] == 0:
    k = True
for idx in range(n):
    if idx in check:
        continue
    cur = idx
    tmp = 0
    cnt = 0
    min_x = sys.maxsize
    while cur not in check:
        check.add(cur)
        cnt +=1
        tmp += a[cur]
        if min_x >  a[cur]:
            min_x = a[cur]
        cur = b[cur][0]
        
    if k:
        ans += min(tmp + min_x*(cnt-2), tmp +b[0][1]*(cnt+1)+ min_x )
    else:
        ans += tmp + min_x * (cnt - 2)
        k = True
print(ans)