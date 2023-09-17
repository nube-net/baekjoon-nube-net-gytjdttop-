import sys
input = sys.stdin.readline
a,b =map(int, input().split())
room  = [0]*a

for _ in range(b):
    r, s, e = map(int, input().split())
    if room[r-1] <= s:
        room[r-1] = e
        print('YES')
    else:
        print('NO')