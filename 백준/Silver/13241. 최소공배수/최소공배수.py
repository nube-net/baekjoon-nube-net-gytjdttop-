import sys

a,b = map(int, sys.stdin.readline().split())
if b>a :
    tmp= b
    b=a
    a=tmp
c=a*b
while a%b != 0 :
    tmp = a%b
    a=b
    b=tmp
print(c//b)

