import  sys
input = sys.stdin.readline


n, m, k = map(int,input().split())
stack= []
if m+k > n+1 or k*m < n:
    print(-1)
else:
    idx = 0
    cnt = 0
    ans = [[] for _ in range(m)]
    for i in range(1,n+1):
        cnt += 1
        ans[idx].append(i)
        if cnt >= k or m-idx > n-i:
            idx += 1
            cnt = 0
    for i in ans:
        while i:
            print(i.pop(), end=" ")