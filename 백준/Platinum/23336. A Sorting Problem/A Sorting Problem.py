import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    global ans
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            ans += len(left) - left_idx
            right_idx += 1

    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

ans = 0
n = int(input())
arr = list(map(int, input().split()))
merge_sort(arr)
print(ans)