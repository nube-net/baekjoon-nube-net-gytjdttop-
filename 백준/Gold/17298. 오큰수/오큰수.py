import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result =[ -1 for _ in range(n)]
stack = [] 

for i in range(n - 1, -1, -1):  
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1]
    stack.append(arr[i])

print(*result)
