n, k = map(int,input().split())
tall = list(map(int,input().split()))
cost = 0
list1 =[] 
for i in range(1,len(tall)) :
    list1 += [(tall[i]-tall[i-1])]

list1.sort()
for k in range(0,n-(k)) :
    cost += list1[k]

print(cost)