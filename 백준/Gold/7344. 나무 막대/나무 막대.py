import sys
from collections import deque
import bisect
input = sys.stdin.readline

t = int(input())
for __ in range(t):
    n = int(input())
    tmp = list(map(int, input().split()))
    a =[]
    for i in range(0,n+n,2):
        a.append((tmp[i],tmp[i+1]))
    a.sort()
    q = deque(a)
    ans = 0
    
    while q:
        ans+=1
        cur = q.popleft()
        l = len(q)
        for _ in range(l):
            l,w = q.popleft()
            if cur[0] <=l and cur[1] <=w:
                cur = (l,w)
            else:
                q.append((l,w))
    print(ans)
                
        
    