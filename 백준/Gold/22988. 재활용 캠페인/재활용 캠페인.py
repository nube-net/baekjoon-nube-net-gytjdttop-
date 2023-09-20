import sys
input = sys.stdin.readline

n, X = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
dx = X/2
# 이미 최대치 달성한 통
tmp = 0
while a and a[-1] >= X:
    a.pop()
    tmp += 1

ans=0
n = len(a)
low = 0
high = n-1
while low < high:
    if a[low] + a[high] >= dx:
        ans += 1
        low += 1
        high -= 1
    else:
        low += 1

print(ans+(n-2*ans)//3 + tmp)
