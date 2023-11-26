import collections

Q = collections.deque(["K","O","R","E","A"])
ans = 0

s = input()

for i in range(len(s)):
    if s[i] == Q[0]:
        Q.append(Q.popleft())
        ans += 1
print(ans)