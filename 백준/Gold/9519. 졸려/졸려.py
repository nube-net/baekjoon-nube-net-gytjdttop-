import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
s = deque(input().rstrip())

store = [s.copy()]

while True:
    tmp = []
    k = True
    while s:
        if k:
            tmp.append(s.popleft())
            k = False
        else:
            tmp.append(s.pop())
            k = True
    s = deque(tmp)
    if list(s) == list(store[0]):
        break
    else:
        store.append(s.copy())

a = n % len(store)

print(''.join(store[-a]))
