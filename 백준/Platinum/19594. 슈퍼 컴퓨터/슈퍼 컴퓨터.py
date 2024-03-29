import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n= int(input())
    H = list(map(int,input().split()))
    D = list(map(int,input().split()))
    a = [(i, j) for i, j in zip(H, D)]
    a.sort(key= lambda x:x[1])
    ans = 0
    cur = 0
    time= []
    for h,d in a:
        cur += h
        late = cur - d
        if late < 0:
            late = 0
        time.append(late)

    late_max = 0
    for i in range(n):
        if time[i] > late_max:
            late_max = time[i]
        time[i] = late_max

    ans = max(time[n-1] - a[0][0] + 1, 0)
    for i in range(1, n):
        ans = min(ans, max(time[i-1], time[n-1] - a[i][0] + 1))
    print(ans)
