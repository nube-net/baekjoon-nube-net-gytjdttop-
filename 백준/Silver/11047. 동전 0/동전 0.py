n,k = map(int,input().split())
c=0

a= set([int(input()) for _ in range(n)])
l= len(a)

for o in range(l) :
    i= max(a)
    if k>= i :
        c+=(k//i)
        k%=i
    if k==0 :
        break
    a.remove(i)

print(c)
