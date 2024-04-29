import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
ans = 1
for i in range(n):
    k = False
    cnt = 1
    for j in range(i+1,n):
        if k:
            if a[j]>=a[j-1]:
                break
        else:
            if a[j] < a[j - 1]:
                k=True
            elif a[j] == a[j-1]:
                break
        cnt += 1
    if cnt > ans:
        ans = cnt
print(ans)