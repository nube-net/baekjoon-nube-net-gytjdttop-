import sys
inputF = sys.stdin.readline

n = int(inputF())

points = [int(inputF()) for _ in range(n)]
result = 0

tmp = points.pop()
while points:
    top = points.pop()
    if top >= tmp:
        result += top - (tmp-1)
        top = tmp-1

    tmp = top
print(result)
