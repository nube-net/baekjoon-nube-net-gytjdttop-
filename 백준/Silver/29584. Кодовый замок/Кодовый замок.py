import sys
input = sys.stdin.readline

k, n = map(int, input().split())
x = ord("A")-10
s = list(input().rstrip())
for i in range(len(s)):
    try:
        s[i] = int(s[i])
    except:
        s[i] = ord(s[i])-x
val = sum(s)
s.reverse()
l=len(s)
while True:
    s[0] += 1
    for i in range(l):
        if s[i] == k:
            if i == l-1:
                print("Impossible")
                exit()
            s[i] = 0
            s[i+1] +=1
        else:
            break
    #print(s)
    if val == sum(s):
        for i in range(l):
            if s[i] < 10:
                s[i]= str(s[i])
            else:
                s[i] = chr(s[i]+x)
        s.reverse()
        print("".join(s))
        break
    


