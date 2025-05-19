import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for __ in range(t):
    n = int(input())
    a = list(map(str, input().split()))
    d = deque()
    for i in a:
        if d:
            if ord(d[0]) >= ord(i):
                d.appendleft(i)
            else:
                d.append(i)
        else:
            d.append(i)
    
    print("".join(d))