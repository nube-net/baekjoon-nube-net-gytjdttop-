import sys
input = sys.stdin.readline

n,d,k,c = map(int,input().split())
a = [int(input()) for _ in range(n)]
a = a + a[:k-1]
cnt = [0 for _ in range(d+1)]
cnt[c]+=1
cur=1
ans=1
length = 0
for i in range(n+k-1):
    length += 1
    if cnt[a[i]] == 0:
        cur += 1
    cnt[a[i]] += 1
    
    if length > k:
        cnt[a[i-k]] -= 1
        if cnt[a[i-k]] ==0:
            cur -= 1
    
    ans = max(ans,cur)
print(ans)
