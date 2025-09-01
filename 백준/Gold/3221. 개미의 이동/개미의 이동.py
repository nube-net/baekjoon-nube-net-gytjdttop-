import sys
from collections import deque
input = sys.stdin.readline

l, t = map(int, input().split())
n = int(input())
ants = [list(map(str,input().split())) for _ in range(n)]
ans = []
for idx, d in ants:
    i = int(idx)
    if d == "L":
        cur = i-t
    else:
        cur = i+t
        
    if cur < 0:
        x = abs(cur)%l
        if (abs(cur)//l)%2:
            ans.append(l-x)
        else:
            ans.append(x)
    elif cur >= l:
        cur -= l
        x = abs(cur)%l
        if (cur//l)%2:
            ans.append(x)
        else:
            ans.append(l-x)
    else:
        ans.append(cur)

ans.sort()
print(*ans)