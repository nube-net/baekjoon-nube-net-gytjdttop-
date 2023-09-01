import sys
input = sys.stdin.readline

n = int(input())

item = []
tmp = 0
for _ in range(n):
    x,y = map(int, input().split())
    item.append([x, y])
    tmp += y
item.sort()

a = tmp/2
s = 0
for i in range(n):
    s += item[i][1]
    if s >= a:
        print(item[i][0])
        break
