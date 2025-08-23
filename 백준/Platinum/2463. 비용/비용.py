import sys
input = sys.stdin.readline
MOD = 10**9
n,m= map(int, input().split())
arr = []
val = 0
for _ in range(m):
    x,y,w = map(int, input().split())
    val += w
    val %= MOD
    if x < y:
        arr.append((w,x,y))
    else:
        arr.append((w, y, x))
arr.sort()
S = [i for i in range(n+1)]
cnt = [ [1,0] for _ in range(n+1) ] # 원소개수,  중복개수

def find(a):
    if S[a] != a:
        S[a] = find(S[a])
    return S[a]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    S[root_b] = root_a
    cnt[root_a][0] += cnt[root_b][0] # 원소개수,  중복개수
    cnt[root_a][1] += cnt[root_b][1]


ans = 0
while arr:
    w,x,y = arr.pop()
    if find(x) == find(y):
        val -= w
        continue
    union(find(x),find(y))
    cur = find(x)
    ans += (cnt[cur][0]*(cnt[cur][0] -1)//2 - cnt[cur][1])*val
    val -= w
    cnt[cur][1]= cnt[cur][0]*(cnt[cur][0] -1)//2
    ans%= MOD
print(ans%MOD)

