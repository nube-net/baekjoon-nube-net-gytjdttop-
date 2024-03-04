import sys
from collections import deque
input = sys.stdin.readline

a,b,c = map(int, input().split())
# x = x*2, y -= x

visited = set()
q = deque()
q.append((a,b,c))
visited.add((a,b,c))

while q:
    a,b,c = q.popleft()
    if a == b and b == c:
        print(1)
        exit()
        
    # a b
    if a < b:
        tmp = (a*2, b-a, c)
        if tmp not in visited:
            visited.add(tmp)
            q.append(tmp)
    if a > b:
        tmp = (a-b, b*2, c)
        if tmp not in visited:
            visited.add(tmp)
            q.append(tmp)
    # a c
    if a < c:
        tmp = (a*2,b,c-a)
        if tmp not in visited:
            visited.add(tmp)
            q.append(tmp)
    if a > c:
        tmp = (a-c,b,c*2)
        if tmp not in visited:
            visited.add(tmp)
            q.append(tmp)

    # b c
    if b < c:
        tmp = (a,b*2,c-b)
        if tmp not in visited:
            visited.add(tmp)
            q.append(tmp)
    if b > c:
        tmp = (a,b-c,c*2)
        if tmp not in visited:
            visited.add(tmp)
            q.append(tmp)
print(0)