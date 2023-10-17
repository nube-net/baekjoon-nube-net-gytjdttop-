import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()

low = 1
high = a[-1]
x = 1000000001
ans = 0
while low <= high:
    mid = (low+high)//2
    tmp = 0

    for i in a:
        if i <= mid:
            tmp += i
        else:
            tmp += mid

    if tmp > m:
        high = mid-1
    else:
        if x > tmp:
            ans = mid
        low = mid + 1

print(ans)


