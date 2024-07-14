import sys
from collections import deque
from heapq import heappop, heappush,heapify
input = sys.stdin.readline
t = int(input())

for __ in range(t):
    n = int(input())
    s = input().rstrip()
    ans=0
    odd = []
    even = []
    for i in range(n):
        if s[i] == 'T':
            if i%2:
                odd.append(i)
            else:
                even.append(i)

    if len(odd) != len(even):
        print(-1)
    else:
        for i in range(len(odd)):
            ans += abs(even[i]-odd[i])
        print(ans)