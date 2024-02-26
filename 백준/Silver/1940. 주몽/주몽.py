import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = list(map(int, input().split()))
a.sort()

low, high = 0, n-1
cnt = 0
tmp = 0
while low < high:
    tmp = a[low] + a[high]
    if tmp == m:
        cnt += 1
        low += 1
        high -= 1
    elif tmp < m:
        low += 1
    elif tmp > m:
        high -= 1

print(cnt)