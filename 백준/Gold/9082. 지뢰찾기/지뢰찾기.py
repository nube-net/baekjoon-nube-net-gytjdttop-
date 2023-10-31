import sys
from heapq import heappop,heappush
input = sys.stdin.readline

T = int(input())
for __ in range(T):
    n = int(input())
    Q = []
    cnt = [int(i) for i in input().strip()]
    a = list(str(input().strip()))
    print((sum(cnt)+2)//3)