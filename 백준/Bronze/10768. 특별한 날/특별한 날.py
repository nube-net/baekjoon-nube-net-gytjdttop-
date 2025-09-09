import sys

input = sys.stdin.readline

m = int(input())
d = int(input())
if m ==2 and d == 18:
    print("Special")
elif m > 2:
    print("After")
elif m == 1:
    print("Before")
else:
    if d < 18:
        print("Before")
    else:
        print("After")