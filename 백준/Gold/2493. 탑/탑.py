import sys
inputF = sys.stdin.readline

n = int(inputF())
tower = list(map(int, inputF().split()))

stack = []
result = [0]*n

for i in range(n-1,-1,-1):
    high = tower.pop()

    if stack:
        while stack:
            if stack[-1][0] <= high:
                x, y = stack.pop()
                result[y] = i+1
                continue
            break

    stack.append((high, i))

print(*result)