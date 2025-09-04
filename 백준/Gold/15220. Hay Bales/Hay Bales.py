import sys

input = sys.stdin.readline
#15220
s = list(input())
l = len(s)
ans = 0
while True:
    k= True
    for i in range(l-2):
        if (s[i],s[i+1],s[i+2]) == ("P","C","C") :
            s[i] = "C"
            s[i+1] = "C"
            s[i+2] = "P"
            k= False
            break
        elif (s[i], s[i + 1], s[i + 2]) == ("P", "P", "C"):
            s[i] = "C"
            s[i + 1] = "P"
            s[i + 2] = "P"
            k= False
            break
    if k:
        for i in range(l - 2):
            if (s[i],s[i+1],s[i+2]) == ("P","C","P") :
                s[i] = "C"
                s[i + 1] = "P"
                s[i + 2] = "P"
                k= False
                break
            elif (s[i], s[i + 1], s[i + 2]) == ("C", "P", "C"):
                s[i] = "C"
                s[i + 1] = "C"
                s[i + 2] = "P"
                k= False
                break
    if k:
        break
    else:
        ans +=1
        
    
print(ans)