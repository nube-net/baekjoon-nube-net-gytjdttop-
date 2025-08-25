import sys
input = sys.stdin.readline

def find(a):
    if S[a] != a:
        S[a] = find(S[a])
    return S[a]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    S[root_b] = root_a
    
n =int(input())
m = int(input())
e =[[] for _ in range(n+1)]
S = [i for i in range(n+1)]
for _ in range(m):
    x,u,v= map(str, input().split())
    u,v = int(u),int(v)
    if x=="F":
        if u < v:
            union(u, v)
        else:
            union(v, u)
    else:
        e[u].append(v)
        e[v].append(u)
        

for a in e:
    a.sort()
    if len(a) >= 2:
        for i in range(1,len(a)):
            union(a[0],a[i])
ans =set()
for i in range(1,n+1):
    ans.add(find(i))
print(len(ans))


        
