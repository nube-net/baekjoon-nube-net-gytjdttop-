import sys
from collections import deque
input= sys.stdin.readline

n = int(input())
a = [i for i in range(1,n+1)]
q = deque(a)
ans = []
while q:
    ans.append(q.popleft())
    if q:
        q.append(q.popleft())
print(*ans)
