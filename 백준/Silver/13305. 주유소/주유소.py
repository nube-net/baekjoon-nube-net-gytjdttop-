import sys

n = int(sys.stdin.readline())
road = list(map(int,sys.stdin.readline().split()))
city =list(map(int,sys.stdin.readline().split()))
result=0
a= city[0]
b= road[0]
for i in range(1,len(city)-1) :
    if city[i] <= a :
        result += a*b
        a=city[i]
        b=road[i]
        if i == n-1 :
            break
    else :
        b+= road[i]
    if i == len(city)-2 :
        result += a*b
        break

print(result)