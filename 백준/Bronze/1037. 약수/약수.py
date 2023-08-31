#a(a!=1,n)

import sys
input= sys.stdin.readline

n = input()

num = list(map(int, input().split()))

num.sort()
a=num[0]
b=num[-1]

print(a*b)