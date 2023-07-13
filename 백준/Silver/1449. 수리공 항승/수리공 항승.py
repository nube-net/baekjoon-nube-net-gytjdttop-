n, L = map(int, input().split())
list1 = list(map(int,input().split()))
list1 += [0]
list1.sort()
start = 1
result = 0
key = 0
L1 = L

for i in range(1, len(list1)):
    if start == 1:
        result += 1
    else :
        if L1-1 >= (list1[i] - list1[i-1]) :
            L1 -= (list1[i] - list1[i-1])
            continue
        else :
            L1 = L
            start = 1
            result +=1 

    start = 0


print(result)