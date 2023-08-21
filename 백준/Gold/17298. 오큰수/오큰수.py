import sys
from collections import deque
input =sys.stdin.readline

n = int(input())
num =  list(map(int,  input().split()))
result  = deque()
stack = []
result.appendleft(-1)
while num:
    tmp = num.pop()
    
    while stack:
        if stack[-1] > tmp:
            result.appendleft(stack[-1])
            break
        else:
            stack.pop()
            if not stack:
                result.appendleft(-1)
    stack.append(tmp)
result =list(result)
print(*result)

