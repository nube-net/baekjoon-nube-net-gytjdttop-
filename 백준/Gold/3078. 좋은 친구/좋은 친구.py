import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
name = deque()
Q = deque()
dp = [0]*(21)
for _ in range(n):
    name.append(len(input().rstrip()))

while len(Q) != k+1:
    tmp = name.popleft()
    dp[tmp] += 1
    Q.append(tmp)

ans = 0
while Q:
    tmp = Q.popleft()
    ans += dp[tmp]-1
    dp[tmp] -= 1
    if name:
        tmp = name.popleft()
        dp[tmp] += 1
        Q.append(tmp)

print(ans)