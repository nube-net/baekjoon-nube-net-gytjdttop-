import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, l, k = map(int, input().split())
    a = [list(map(float, input().split())) for _ in range(n)]
    arr = []
    for x, id in a:
        t = l - x if id > 0 else x
        arr.append((t, id))

    arr.sort()
    left, right = 0, n - 1
    tmp = []

    i = 0
    while i < n:
        cur = (i + 1 < n and arr[i][0] == arr[i + 1][0])
        if cur:
            ants = [a[left], a[right]]
            tmp += sorted(ants, key=lambda x: x[1])
            left += 1
            right -= 1
            i += 2
        else:
            tmp.append(a[left] if arr[i][1] < 0 else a[right])
            left += arr[i][1] < 0
            right -= arr[i][1] > 0
            i += 1
    # print(i, left, right)
    print(int(tmp[k - 1][1]))

    
    
    
    
    
    
    