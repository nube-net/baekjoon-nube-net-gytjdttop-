import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
val = sum(arr) - m

ans = 0
for i in range(n):
    tmp = min(arr[i], val//(n-i))

    ans += tmp**2
    val -= tmp
print(ans%(2**64))