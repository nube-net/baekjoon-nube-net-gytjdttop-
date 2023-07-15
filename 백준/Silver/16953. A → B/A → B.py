import sys

def code(a,b,c):
    if a==b:
        return c
    elif a<b:
        return -1
    
    if a%2 == 1:
        if a%10 !=1:
            return -1
        else:
            return code(a//10,b,c+1)
    else:
        return code(a//2,b,c+1)


a, b = map(int, sys.stdin.readline().split())
c=1
print(code(b,a,c))

