import sys
import heapq
input = sys.stdin.readline
push = heapq.heappop
pop = heapq.heappop

T = int(input())
for z in range(T):
    n=int(input())
    a=[]
    for i in range(n) :
        a.append(list(map(int,input().split())))
    a.sort()
    heapq.heapify(a)
    tmp=[]
    store =[]

    for num in range(n) :
        if num == 0:
            tmp= pop(a)
            c=1
        else :
            store = pop(a)
            if tmp[1] > store[1] :
                c+=1
                tmp= store


    print(c)


