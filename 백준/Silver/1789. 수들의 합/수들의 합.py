import sys

n = int(sys.stdin.readline())
c=0
for i in range(1,n+1) :
    if n>=i:
        n-=i
    else :
        break
    c+=1

print(c)