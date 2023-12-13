import sys
input =sys.stdin.readline

l, k,c=map(int, input().split())
a = list(map(int, input().split()))
a.append(l)
a = set(a)
a = list(a)
a.sort()
low = 1
high = l
ans = [0,0]
while low <= high:  # mid 최적 탐색
    mid = (low +high)//2
    # print(low,mid,high)
    cnt = 0
    k = True
    pre = l
    for i in range(len(a)-1,-1,-1):
        # print("+",a[i])
        if pre-a[i] > mid:
            if a[i+1]-a[i] > mid:
                k= False
                break
            cnt += 1
            pre = a[i+1]
            if cnt == c:
                break

    if cnt < c:
        pre = a[0]
    if pre > mid:
        k = False
    if k:
        high = mid -1
        ans = [mid,pre]
    else:
        low = mid +1
print(*ans)








