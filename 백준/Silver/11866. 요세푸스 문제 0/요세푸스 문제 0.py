import sys
input = sys.stdin.readline

a,b = map(int, input().split())

circle = []
for i in range(1,a+1) :
    circle.append(i)

result =[]
tmp=0
c=0
while circle :
    c+=1
    tmp= circle[0]
    circle.remove(tmp)

    if c==b :
        c=0
        result.append(tmp)
    else :
        circle.append(tmp)
ff=str(result)
ff=ff.replace('[','<')
ff=ff.replace(']','>')
print(ff)
