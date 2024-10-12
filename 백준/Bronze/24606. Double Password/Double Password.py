import sys
input = sys.stdin.readline

a = list(input())
b = list(input())
x= 0
for i in range(4):
    if a[i] != b[i]:
        x += 1

ans =1
for _ in range(x):
    ans *=2
print(ans)