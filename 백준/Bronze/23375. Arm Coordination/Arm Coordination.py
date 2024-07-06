import sys
input = sys.stdin.readline

x,y = map(int, input().split())
r = int(input())
a = [x-r,x+r]
b = [y-r,y+r]

print(x-r,y+r)
print(x-r,y-r)
print(x+r,y-r)
print(x+r,y+r)