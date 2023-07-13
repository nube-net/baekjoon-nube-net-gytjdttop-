import sys


n = int(sys.stdin.readline())

town = []
Map = set()  # 집이 있는 곳

for y in range(n):
    town = (list(sys.stdin.readline().rstrip()))
    for x in range(n):
        if town[x] == "1":
            Map.add((x,y))

result = []
stack = []
while Map:
    if not stack:
        stack.append(Map.pop())
        result.append(0)
        result[-1] += 1
    else:
        x,y = stack[-1]
        if (x+1, y) in Map:
            stack.append((x+1, y))
            Map.remove((x+1, y))
            result[-1] += 1
            continue
        elif (x-1, y) in Map:
            stack.append((x-1, y))
            Map.remove((x-1, y))
            result[-1] += 1
            continue
        elif (x, y+1) in Map:
            stack.append((x, y+1))
            Map.remove((x, y+1))
            result[-1] += 1
            continue
        elif (x, y-1) in Map:
            stack.append((x, y-1))
            Map.remove((x, y-1))
            result[-1] += 1
            continue
        stack.pop()

result.sort()
print(len(result))
for k in result:
    print(k)