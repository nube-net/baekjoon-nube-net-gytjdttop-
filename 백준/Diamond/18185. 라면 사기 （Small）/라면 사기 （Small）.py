import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split())) + [0, 0]
ans = 0

for i in range(n):
    # print(i)
    if a[i] > 0 :
        if a[i + 1] > a[i + 2]:
            d = min(a[i], a[i+1]-a[i+2])
            a[i] -= d
            a[i+1] -= d
            ans += d*5
            # print(a, ans)

        if a[i]>0:
            d = min(a[i:i+3])
            if d > 0:
                ans += d*7
                a[i] -= d
                a[i + 1] -= d
                a[i + 2] -= d
                # print(a, ans)

            if a[i] > 0:
                ans += a[i]*3
                a[i] = 0
                # print(a, ans)
print(ans)