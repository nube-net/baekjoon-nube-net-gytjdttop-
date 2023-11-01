import sys
input = sys.stdin.readline

h, w = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for _ in range(h):
    loc = False
    cnt = 0
    for i in range(w):
        if a[i] > 0:
            if loc:
                ans += cnt
            loc = True
            cnt = 0
        else:
            cnt += 1
        a[i] -= 1
    # print(ans)
print(ans)