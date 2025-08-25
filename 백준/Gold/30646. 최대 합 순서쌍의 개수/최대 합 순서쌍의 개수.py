import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dic ={}
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
    cur = a[i-1]
    dp[i]= dp[i-1]+cur
    if cur in dic:
        dic[cur].append(i-1)
    else:
        dic[cur] = [i-1]
ans = 0
cnt = 1
for key in dic:
    st,end = dic[key][0], dic[key][-1]
    x= dp[end+1]-dp[st]
    if ans < x:
        ans = x
        cnt =1
    elif ans == x:
        cnt +=1
print(ans,cnt)