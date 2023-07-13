import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    if (n >= 7) or n==5:
        print(1)
    elif n == 4:
        print(2)
    else :
        print(0)