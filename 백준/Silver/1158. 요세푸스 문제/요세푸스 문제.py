from collections import deque
n, k = map(int, input().split())
q = deque([i for i in range(1,n+1)])
cnt = 0
print("<", end="")
while len(q) > 1:
    cnt += 1
    cur = q.popleft()
    if cnt == k:
        cnt = 0
        print(cur,end=", ")
        continue
    q.append(cur)
print(q[0], end=">")
