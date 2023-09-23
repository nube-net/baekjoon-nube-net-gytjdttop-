import sys
import math
input = sys.stdin.readline
n, m = map(int, input().split())
nums = [0]*m

for _ in range(n):
    tmp = list(map(int, input().split()))

    for i in range(m):
        nums[i] += tmp[i]
a= int(input())
ans = 0
for i in range(m-a+1):
    ans = max(ans, sum(nums[i:i+a]))

print(ans)