import sys

n = int(sys.stdin.readline())

c5=0
c2=0
k= False

while n>=0 :
    if n%5 == 0:
        c5 =n//5
        k=True
        break
    else:
        c2 +=1
    n-=2

if k:
    print(c5+c2)
else:
    print(-1)
