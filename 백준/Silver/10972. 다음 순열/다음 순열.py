n = int(input())
arr = list(map(int, input().split()))
if arr == [i for i in range(n, 0, -1)]:
    print(-1)
else:
    for idx in range(n-1, -1, -1):
        if arr[idx - 1] < arr[idx]:
            break
            
    for j in range(n-1, -1, -1):
        if arr[j] > arr[idx- 1]:
            break

    arr[idx - 1], arr[j] = arr[j], arr[idx - 1]
    arr[idx:] = reversed(arr[idx:])
    print(*arr)