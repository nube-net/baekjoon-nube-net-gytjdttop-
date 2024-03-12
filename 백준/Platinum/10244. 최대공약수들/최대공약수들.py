from math import  gcd
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break

    arr = [int(input()) for _ in range(n)]
    S = set()
    for x in range(1, 101):
        a = 0  # gcd(0,a) = a
        for i in arr:
            if gcd(a, i) % x == 0:
                a = gcd(a, i)
                if a == x:
                    S.add(x)
            else:
                a = 0
            # print(x,a)
    print(len(S))