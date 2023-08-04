import sys
inputF = sys.stdin.readline

n, m = map(int, inputF().split())
stack = []

for _ in range(m):
    stack.append(1)

while stack:
    if len(stack) == m:
        print(*stack)
        tmp = stack.pop()
        if tmp == n:
            continue
        else:
            stack.append(tmp+1)
    else:
        tmp = stack.pop()
        if tmp == n:
            continue
        else:
            for _ in range(m- len(stack)):
                stack.append(tmp+1)
