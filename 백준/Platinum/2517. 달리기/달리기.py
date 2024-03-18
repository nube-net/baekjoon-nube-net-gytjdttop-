import sys
input = sys.stdin.readline
def merge(left, right):
    return left + right

def build(stree, node, left, right):
    if left == right:
        stree[node] = arr[left]
        return stree[node]

    mid = left + (right - left) // 2
    l_val = build(stree, 2 * node, left, mid)
    r_val = build(stree, 2 * node + 1, mid + 1, right)
    stree[node] = merge(l_val, r_val)
    return stree[node]

def query(start, end, node, left, right):
    if end < left or start > right:
        return 0

    if start <= left and right <= end:
        return stree[node]

    mid = left + (right - left) // 2
    l_val = query(start, end, 2 * node, left, mid)
    r_val = query(start, end, 2 * node + 1, mid + 1, right)
    return merge(l_val, r_val)

def update(idx, node, left, right):
    if idx < left or idx > right:
        return stree[node]
    if left == right:
        stree[node] = 1
        return stree[node]

    mid = left + (right - left) // 2
    l_val = update(idx, 2 * node, left, mid)
    r_val = update(idx, 2 * node + 1, mid + 1, right)
    stree[node] = merge(l_val, r_val)
    return stree[node]
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge1(left_half, right_half)

def merge1(left, right):
    global ans
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx][0] <= right[right_idx][0]:
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
arr = [(-int(input()), idx) for idx in range(n)]  # 인덱스도 같이 저장
sorted_arr = merge_sort(arr)
move = [0]*n
stree = [0] * (4 * (n + 1))
for i in range(n):
    num,idx = sorted_arr[i]
    move[idx] = i
# print(sorted_arr)
#print(move)
for i in range(n):
    idx = move[i] +1
    print(query(1,idx, 1, 1, n)+1)
    update(idx, 1, 1, n)

