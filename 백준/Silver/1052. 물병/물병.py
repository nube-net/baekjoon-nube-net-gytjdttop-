import sys
input = sys.stdin.readline

n, k = map(int, input().split())
if n <= k:
    print(0)
else:
    a = 0
    while True:
        cnt = bin(n+a).count('1')
        if cnt <= k:
            break
        a += 1
    print(a)

