import sys
input = sys.stdin.readline

n = int(input())
a= 0
b= 0

x = 1
while True:
    if n <= x:
        break
    else:
        n -= x
        x += 1
if x%2 == 1:
    a = x-n +1
    b = n
else:
    a = n
    b = x-n +1
print(f"{a}/{b}")