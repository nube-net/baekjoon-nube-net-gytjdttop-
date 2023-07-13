import sys
input = sys.stdin.readline

n = int(input())

two = 0
five = 0
for i in range(1,n+1):
    if i % 2 == 0:
        a = i
        while a % 2 == 0:
            a = a // 2
            two += 1
    if i % 5 == 0:
        b = i
        while b % 5 == 0:
            b = b // 5
            five += 1

print(min(two, five))
