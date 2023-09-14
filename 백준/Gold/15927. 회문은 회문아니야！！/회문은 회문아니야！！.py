import sys

s = sys.stdin.readline().rstrip()
l = len(s)
if l == s.count(s[0]):
    print(-1)
else:
    if l%2 == 0:
        if s[:l//2] == s[l-1:l//2-1:-1]:
            print(l-1)
        else:
            print(l)
    else:
        if s[:l // 2] == s[l-1: l // 2:-1]:
            print(l - 1)
        else:
            print(l)
