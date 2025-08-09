import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().strip()
    l, r = 0, len(s) - 1
    cnt = 0
    ans = 1
    while l <= r:
        cnt += 1
        if s[l] != s[r]:
            ans = 0
            break
        l += 1
        r -= 1

    if ans == 1 and len(s) % 2 == 0:
        cnt += 1
    print(ans, cnt)
