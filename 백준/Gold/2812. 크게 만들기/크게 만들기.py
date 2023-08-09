import sys
from collections import deque
inputF = sys.stdin.readline

n, k = map(int, inputF().split())
s = inputF().rstrip()
s = deque(s)
l = n-k
stack = []
stack.append(s.popleft())

while s:
    tmp = s.popleft()

    while k > 0 and stack:
        if stack[-1] < tmp:
            stack.pop()
            k -= 1
        else:
            break

    stack.append(tmp)
while len(stack) > l:
    stack.pop()
result = ''.join(_ for _ in stack)
print(result)
