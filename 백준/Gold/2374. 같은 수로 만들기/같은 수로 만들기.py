import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0

stack = []
stack.append(a[0])
if n == 1:
    print(0)
else:
    for i in range(1,n):
        x = a[i]
        if stack[-1] >= x:
            stack.append(x)
        else:
            ans += x-stack[-1]
            while stack:
                if stack[-1] <= x:
                    stack.pop()
                else:
                    break
            stack.append(x)
    if stack:
        ans += stack[0]-stack[-1]
    print(ans)
