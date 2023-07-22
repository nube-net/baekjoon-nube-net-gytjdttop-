import sys 

n = int(sys.stdin.readline())
c=0
for i in range(n):
    tmp = set()
    store = ''

    a= sys.stdin.readline().rstrip()
    
    for k in range(len(a)):
        if a[k] in tmp:
            if a[k] != store:
                break
        else:
            tmp.add(a[k])
            store = a[k]
        
        if k == len(a)-1:
            c+=1
print(c)