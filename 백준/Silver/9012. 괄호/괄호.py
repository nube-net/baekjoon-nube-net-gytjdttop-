import sys
input = sys.stdin.readline

n= int(input())

for i in range(n) :
    a= input().rstrip()
    c=0
    for k in range(len(a)):
        if c <0 :
            break
        if k==0 and a[k] !="(":
            c=1
            break
        if k== len(a)-1 and a[k] !=")":
            c=1
            break
        if a[k] =="(":
            c+=1
        else :
            c-=1
    if c==0 :
        print("YES")
    else :
        print("NO")