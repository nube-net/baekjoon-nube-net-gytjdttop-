import sys
input = sys.stdin.readline
MAX = sys.maxsize

def cal(x):
    if x:
        cnt = 0
        t = x
        while t % 2 == 0:
            t //= 2
            cnt += 1

        cnt2 = 0
        t = x
        while t % 5 == 0:
            t //= 5
            cnt2 += 1
        return cnt, cnt2
    else:
        return MAX, MAX

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp2 = [[MAX for _ in range(n)] for _ in range(n)]
dp5 = [[MAX for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if a[i][j] == 0:
            dp5[i][j] = MAX
            dp2[i][j] = MAX
            continue

        cnt, cnt2 = cal(a[i][j])

        if i == 0 and j == 0:
            dp2[i][j] = cnt
            dp5[i][j] = cnt2
            continue

        x, y = MAX, MAX
        if i > 0:
            x = dp2[i-1][j]
        if j > 0:
            y = dp2[i][j-1]
        dp2[i][j] = min(x, y)
        if dp2[i][j] < MAX:
            dp2[i][j] += cnt

        x, y = MAX, MAX
        if i > 0:
            x = dp5[i-1][j]
        if j > 0:
            y = dp5[i][j-1]
        dp5[i][j] = min(x, y)
        if dp5[i][j] < MAX:
            dp5[i][j] += cnt2

print(min(dp2[n-1][n-1], dp5[n-1][n-1]))

