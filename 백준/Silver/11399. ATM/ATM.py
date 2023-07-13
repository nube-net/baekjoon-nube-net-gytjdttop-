n = int(input())
c=0
a=[]
a += map(int, input().split())
a.sort()

for i in range(len(a)):
    c+= int(int(a[i])*n)
    n-=1
    
print(c)