import sys
input = sys.stdin.readline

t = int(input())
for __ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = []
    tmp = []
    k = False
    for i in range(n):
        if arr[i] > i:
            k = True
            break
    if k:
        print("IMPOSSIBLE")
        continue

    for val in arr[::-1]:
        tmp.sort()
        cur = val + 1
        cnt = 0
        for i in tmp:
            if cur + cnt >= i:
                cnt += 1
        ans.append(cur + cnt)
        tmp.append(cur+cnt)
    print(*ans[::-1])

