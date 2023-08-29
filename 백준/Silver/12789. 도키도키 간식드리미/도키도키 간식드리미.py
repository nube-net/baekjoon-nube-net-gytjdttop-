import sys
input = sys.stdin.readline

n = int(input())
order = list(map(int, input().split()))
stack = []

idx = 1
for i in order:
    if i == idx:
        idx += 1
    else:
        stack.append(i)

    while stack:
        if stack[-1] == idx:
            stack.pop()
            idx += 1
        else:
            break

if stack:
    print('Sad')
else:
    print('Nice')