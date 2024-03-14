import sys
input = sys.stdin.readline

stack = []
ans = 0
n = int(input())
for _ in range(n):
    cur = int(input())
    while stack and stack[-1][0] < cur:
        ans += stack.pop()[1]

    if stack:
        if stack[-1][0] == cur:
            tmp = stack.pop()
            ans += tmp[1]
            if stack:
                ans +=1
            tmp[1] += 1
            stack.append(tmp)
        else:
            stack.append([cur, 1])
            ans += 1
    else:
        stack.append([cur,1])

print(ans)