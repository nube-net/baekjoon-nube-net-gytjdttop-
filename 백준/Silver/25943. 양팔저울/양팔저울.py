import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
l,r = a[0],a[1]
x = [1,2,5,10,20,50,100]

for i in range(2,n):
    cur = a[i]
    if l <= r:
        l += cur
    else:
        r += cur
dif = abs(l-r)
ans = 0

for i in x[::-1]:
    if dif >= i:
        ans += dif//i
        dif %= i
print(ans)