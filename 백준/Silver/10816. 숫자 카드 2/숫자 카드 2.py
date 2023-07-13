import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split())) #cards

m = int(input())
b = list(map(int, input().split()))

dic ={}
for i in b :
    if not(i in dic) :
        dic[i] = 0

for k in a :
    if k in dic :
        dic[k] += 1
result=[]
for o in b :
    result.append(dic[o])

print(*result)