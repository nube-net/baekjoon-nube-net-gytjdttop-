import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
n1= []
n1 +=num
k = 0
r1="1 1"
r2="1 1"
c=0
for j in range(0,3):
    st = 0
    for i in range(0,len(num)):
        if num[i] != i + 1 and k == 0:
            st = i
            k = 1
        elif k == 1 and num[i] == st + 1:
            num[st:i + 1] = num[st:i + 1][::-1]
            k = 0
            if j ==0 :
                r1 =f"{st + 1} {i + 1}"
            else :
                r2 = f"{st + 1} {i + 1}"
            c+=1
            break
if c== 3:
    num= n1
    for j in range(0,2):
        st = n
        for i in range(len(num)-1,-1,-1):
            if num[i] != i+1  and k == 0:
                st = i
                k = 1
            elif k == 1 and num[i] == st+1 :
                num[i:st+1] = num[i:st+1][::-1]
                k = 0
                if j ==0 :
                    r1 =f"{i+1} {st+1}"
                else :
                    r2 = f"{i+1} {st+1}"
                break
print(r1)
print(r2)

