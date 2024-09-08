import sys
from collections import  deque
input = sys.stdin.readline

s = list(input().rstrip())
a,b,c = 0,0,0
ans = 0
for i in s:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1
    else:
        c += 1

    if a and b and c:
        ans = max(a,b,c,ans)
        a-=1
        b-=1
        c-=1
print(ans)
