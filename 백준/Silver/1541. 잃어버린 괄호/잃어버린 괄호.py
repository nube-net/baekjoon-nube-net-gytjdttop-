n = input() 
a=0
b=0
k = 0
k1=""
tmp = 0

for i in range(len(n)):
    if i == len(n) - 1 and b!=0:
        k1 += n[i]
        k += int(k1)
        tmp -= int(k)
        break
    elif i==len(n)-1 and b==0:
        k1 += n[i]
        k += int(k1)
        tmp +=int(k)
        break

    if a == 0 and n[i] == "-"and b==0:
        b+=1
        k += int(k1)
        tmp += int(k)#
        k = 0
        k1=""
        a = 1
    elif a == 1 and n[i] == "-":
        k += int(k1)
        a = 0
        tmp -= int(k)#
        k = 0
        k1=""
    elif a == 0 and n[i] == "-":
        k += int(k1)
        tmp -= int(k)#
        k = 0
        k1=""
        a = 1
    else:
        if n[i] != "+":
            k1 += n[i]
        else :
            k += int(k1)
            k1=""

print(tmp)  
