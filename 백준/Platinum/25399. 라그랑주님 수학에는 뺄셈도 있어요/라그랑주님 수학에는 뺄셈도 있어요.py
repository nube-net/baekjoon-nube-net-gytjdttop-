import sys
import math

input = sys.stdin.readline

n = int(input())
ans = []
x = ["+", "-"]
neg = 0
# edge
if n < 0:
    neg = 1
    n = abs(n)

if n == 0:
    print("3")
    print("+ 3")
    print("+ 4")
    print("- 5")
# 1
elif n == 2:
    print(3)
    print(f"{x[0 + neg]} {6}")
    print(f"{x[(1 + neg) % 2]} {3}")
    print(f"{x[(1 + neg) % 2]} {5}")
elif n == int(math.sqrt(n)) ** 2:
    print(1)
    print(f"{x[0 + neg]} {int(math.sqrt(n))}")
# 2, odd
elif n % 2:
    print(2)
    print(f"{x[0 + neg]} {n // 2 + 1}")
    print(f"{x[(1 + neg) % 2]} {n // 2}")
else:  # even
    if n % 4 == 0:
        print(2)
        print(f"{x[0 + neg]} {n // 4 + 1}")
        print(f"{x[(1 + neg) % 2]} {n // 4 - 1}")
    else:
        ######
        S = set()
        for i in range(1, int(math.sqrt(n)) + 1):
            S.add(i ** 2)
        for i in S:
            if (n - i in S) and (n - i != i):
                print(2)
                print(f"{x[0 + neg]} {int(math.sqrt(i))}")
                print(f"{x[(0 + neg) % 2]} {int(math.sqrt(n - i))}")
                exit()
        n += 1
        print(3)
        print(f"{x[(1 + neg) % 2]} {1}")
        print(f"{x[0 + neg]} {n // 2 + 1}")
        print(f"{x[(1 + neg) % 2]} {n // 2}")

