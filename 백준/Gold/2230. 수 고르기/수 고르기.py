import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()

st, end =0, 0
ans = float('inf')
while st != n-1:
    if a[end]-a[st] < m:
        if end == n-1:
            break
        end += 1
    else:
        ans = min(a[end]-a[st], ans)
        st += 1
print(ans)