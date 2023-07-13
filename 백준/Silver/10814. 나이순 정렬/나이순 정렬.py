import sys
input = sys.stdin.readline

n = int(input())
a=[]

for i in range(n) :
    b=input().rstrip()
    b= b.split()
    a.append([int(b[0]),b[1]])
a.sort(key = lambda x : x[0])

for k in a :
    print(f"{int(k[0])} {k[1]}")
