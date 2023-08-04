import sys
from collections import deque
inputF = sys.stdin.readline

a = inputF().rstrip()
a = deque(a)

b = inputF().rstrip()
end = len(b)

stack = []
while a:
    stack.append(a.popleft())

    if len(stack) >= end-1:
        if ''.join(stack[-end:]) == b:
            for _ in range(end):
                stack.pop()

if stack:
    print(''.join(s for s in stack))
else:
    print('FRULA')


