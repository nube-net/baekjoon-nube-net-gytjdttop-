import sys
input = sys.stdin.readline

n = int(input())
dic = {}
for i in range(1,n+1):
    tmp = list(map(int,input().split()))
    dic[i] =set(tmp[1:])
A =set([i for i in range(1,n+1)])
B =set()
flag = True
while flag:
    flag = False
    for i in range(1,n+1):
        a,b=0,0
        for hostility in dic[i]:
            if hostility in A:
                a += 1
            elif hostility in B:
                b += 1
        if (a > b) and (i in A):
            A.remove(i)
            B.add(i)
            flag = True
        elif (b > a) and (i in B):
            B.remove(i)
            A.add(i)
            flag = True
if not A or not B:
    A.remove(1)
    B.add(1)
print(len(A),*A)
print(len(B),*B)