from collections import deque

n, m = map(int, input().split())

result = [-1] * (n + m + 1)
dp = [[] for _ in range(n + m + 1)]
targeted = [0] * (n + m + 1)
Q = deque()

line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))

for x, y in enumerate(line1, start=1):
    dp[x].append(y + n)
    targeted[y + n] += 1

for x, y in enumerate(line2, start=n+1):
    dp[x].append(y)
    targeted[y] += 1

for x in range(1, n + m + 1):
    if targeted[x] == 0:
        Q.append(x)

while Q:
    tmp = Q.popleft()
    if result[tmp] == -1:
        nxt = dp[tmp][0]
        result[tmp] = 1
        result[nxt] = 0
        
        target = dp[nxt][0]
        targeted[target] -= 1
        
        if targeted[target] == 0:
            Q.append(target)

    # 추가되지 않은 노드를 검사하여 큐에 넣음
    if not Q:
        for x in range(1, n + m + 1):
            if result[x] == -1:
                Q.append(x)


print(''.join(map(str, result[1:n+1])))
print(''.join(map(str, result[n+1:n+m+1])))
