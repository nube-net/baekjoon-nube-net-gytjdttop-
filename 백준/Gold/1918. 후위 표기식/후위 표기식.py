import sys
input = sys.stdin.readline

S = list(input().rstrip())

stack = [] 
result = []
cnt = 0
order = {'+': 2, '-': 2, '*': 1, '/': 1, '(': 3, ')': 3}

for s in S:
    if str.isalpha(s):
        result.append(s)
    else:
        if s == '(':
            stack.append(s)
        elif s == ')':
            while True:
                tmp = stack.pop()
                if tmp == '(':
                    break
                else:
                    result.append(tmp)
        else:
            while stack:
                if order[stack[-1]] <= order[s]:
                    result.append(stack.pop())
                else:
                    break
            stack.append(s)
while stack:
    result.append(stack.pop())

print(''.join(result))