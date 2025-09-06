import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    s = input().rstrip()
    ans = 0
    l, h = 0, len(s) - 1
    while l < h:
        if s[l] == s[h]:
            l += 1
            h -= 1
        else:
            if s[l+1:h+1] == s[l+1:h+1][::-1]:
                ans = 1
                break
            if s[l:h] == s[l:h][::-1]:
                ans = 1
                break
            ans = 2
            break
    print(ans)
