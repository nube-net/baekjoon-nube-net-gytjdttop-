import sys
input = sys.stdin.readline

n =int(input())
a = [int(input()) for _ in range(n)]
stack = []
cnt = 0
ans = 0
for cur in a:
    while stack and cur >= stack[-1]:
        stack.pop()
    stack.append(cur)
    if stack:
        ans += len(stack)-1
    
print(ans)