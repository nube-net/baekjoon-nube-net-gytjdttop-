import sys
from math import gcd, lcm

a, b = map(int, input().split())
A,B = map(int, input().split())
y = lcm(b,B)
a *= (y//b)
A *= (y//B)
x = a +A
d = gcd(x,y)
print(x//d,y//d)