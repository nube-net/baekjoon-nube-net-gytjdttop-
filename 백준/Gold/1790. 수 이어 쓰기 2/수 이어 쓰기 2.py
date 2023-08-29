n, k = map(int, input().split())

cnt = [9*(10**(i-1))*i for i in range(10)]
cnt[0] = 0
for i in range(1, 10):
    if k > cnt[i]:
        k -= cnt[i]
    else:
        break
dx = k//i
mod = k%i
ans = 10**(i-1)-1 + dx
if mod ==0:
    if ans > n:
        print(-1)
    else:
        print(str(ans)[-1])
else:
    ans += 1
    if ans > n:
        print(-1)
    else:
        print(str(ans)[mod-1])

