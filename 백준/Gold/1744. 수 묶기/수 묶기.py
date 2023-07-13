import sys
num = int(sys.stdin.readline())
num0 = [sys.stdin.readline().strip() for i in range(num)]

n1 = []#음수
n2 = []#양수
n3 = [0,0] #0 처리용
key =0
for k in num0 :
    if int(k) <0 :
        n1 += [int(k)]
    else :
        n2 += [int(k)]

n1.sort()
if len(n1)%2 != 0 :    
    n3 += [n1.pop()]
n2.sort()
n2.reverse()
result = 0
for j in range(0,len(n1)) :
    if j%2 == 0 :
        result += int(n1[j]*n1[j+1])
if len(n2)%2 != 0 :    
    key = n2.pop()
    if key != 0 :
        result += key
    else :
        n3 += [key]


for o in range(0,len(n2)) :
    if o%2 == 0 :
        if n2[o] ==0 or n2[o+1]==0 :
            if n2[o] ==0 :
                n3+=[n2[o]]
            if n2[o+1] == 0 :
                n3 += [n2[o+1]]
            result += n2[o] + n2[o+1]
        else :
            if n2[o] ==1 or n2[o+1]==1 :
                result += n2[o] + n2[o+1]
            else :
                result += int(n2[o]*n2[o+1])

n3.sort()
if len(n3) == 3 :
    result += n3[0]
else :
    result += n3[0]*n3[1]

print(result)
