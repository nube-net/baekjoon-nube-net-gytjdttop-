import sys
input = sys.stdin.readline

t = int(input())
ans = []
for _ in range(t):
    a,b,c = map(int,input().split())
    d = [a,b,c]
    d.sort()
    
    if a==b and b==c and a==c:
        ans.append(10000+int(a*1000))
    elif a!=b and b!=c and a!=c :
        ans.append(int(d[2])*100)   
    else :
        ans.append(1000+100*(int(d[1])))    
print(max(ans))