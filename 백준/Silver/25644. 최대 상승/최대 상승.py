import sys
input = sys.stdin.readline

n = int(input())
items = list(map(int, input().split()))

MAX = items[-1]
ans = 0

for i in range(n-1,-1,-1):
    if MAX < items[i]:
        MAX = items[i]
    else:
        ans = max(MAX-items[i], ans)
print(ans)
