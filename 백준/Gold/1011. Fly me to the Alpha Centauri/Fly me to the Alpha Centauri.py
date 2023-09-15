import sys

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    d = b - a
    left = 0
    right = 0
    MAX = 0
    i = 1
    while MAX < d:
        # left
        MAX += i
        left += 1
        if MAX >= d:
            break

        # right
        MAX += i
        right += 1
        i+= 1

    print(right + left)