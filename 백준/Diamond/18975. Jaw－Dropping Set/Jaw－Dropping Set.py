import sys
from heapq import heappop, heappush,heapify
input = sys.stdin.readline

t = int(input())
for __ in range(t):
    n = int(input())
    ans = 0
    x = 1
    cnt = n // 2
    if n % 2 == 1:
        cnt += 1
    n = n // 3
    while n >0:
        tmp = n // 2
        if n % 2 == 1:
            tmp += 1
        ans += x*(tmp)**2
        
        #print(n, ans,x)
        x *= 2
        n = n//3
    print(ans+ (cnt)**2)
    
    
