import sys
from collections import deque
input = sys.stdin.readline
from heapq import heappop, heappush, heappushpop, heapify

n, m = map(int, input().split())
Map = []
Q = []
visited = set()
heapify(Q)
for i in range(n):
    a = list(map(int, input().split()))
    Map.append(a)
    if i == 0 or i == n-1:  # 첫줄 혹은 마지막줄
        for j in range(m):
            heappush(Q, (-a[j],(i+1,j+1)))
            visited.add((i+1,j+1))
    else:
        heappush(Q,  (-a[0],(i+1,1)))
        visited.add((i + 1, 1))
        if m != 1:
            heappush(Q, (-a[m-1], (i + 1, m)))
            visited.add((i + 1, m))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
k = int(input())
for _ in range(k):
    __, y = heappop(Q)
    print(*y)


    for i in range(4):
        X, Y= y[0]+dx[i]-1, y[1]+dy[i]-1
        if X <0 or X >=n or Y <0 or Y >= m:
            continue
        if (X+1,Y+1) in visited:
            continue
        else:
            heappush(Q, (-Map[X][Y], (X+1,Y+1)))
            visited.add((X+1,Y+1))



