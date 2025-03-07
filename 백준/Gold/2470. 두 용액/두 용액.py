import sys
import heapq
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()

val = sys.maxsize
ans = []

st = 0
end = n-1
while st < end:
    cur = a[st] + a[end]

    if abs(cur) < abs(val):
        val = cur
        ans = [a[st], a[end]]
        if cur == 0:
            break

    if cur > 0:
        end -= 1
    else:
        st += 1
print(*ans)