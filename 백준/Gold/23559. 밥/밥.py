import sys
input = sys.stdin.readline

n, x = map(int,input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key= lambda x: x[1]-x[0])
ans = 0
for i in range(n):
    if a[i][0] > a[i][1]:
        if x >= (n-i)*1000 + 4000:
            x -= 5000
            ans += a[i][0]
        else:
            x -= 1000
            ans += a[i][1]
    else:
        x -= 1000
        ans += a[i][1]

print(ans)