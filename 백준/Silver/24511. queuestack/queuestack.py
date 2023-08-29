import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
check = list(map(int, input().split()))
value = list(map(int, input().split()))
Q = deque()
for i in range(n):
    if check[i]:
        continue
    else:
        Q.append(value[i])

m = int(input())
tmp = list(map(int, input().split()))
ans = []
for i in tmp:
    Q.appendleft(i)
    ans.append(Q.pop())
print(*ans)