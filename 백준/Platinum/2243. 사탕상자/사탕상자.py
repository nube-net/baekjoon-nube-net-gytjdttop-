import sys
input = sys.stdin.readline
# 세그 트리
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

def update(idx, node, left, right, cnt):
    if idx < left or idx > right:
        return stree[node]
    if left == right:
        stree[node] += cnt
        return stree[node]

    mid = left + (right - left) // 2
    l_val = update(idx, 2 * node, left, mid,cnt)
    r_val = update(idx, 2 * node + 1, mid + 1, right,cnt)
    stree[node] = merge(l_val, r_val)
    return stree[node]

m = int(input())
n = 1000000
arr = [0] * (n + 1) # 전후 체크
stree = [0] * (4 * (n + 1))
build(stree, 1, 1, n)

for _ in range(m):
    a = list(map(int, input().split()))
    if a[0] == 2:
        idx = a[1]  # b맛 사탕
        update(idx, 1, 1, n,a[2])
    else:
        low, high = 1, n
        mid = (low + high) // 2
        while low <= high:
            mid = (low+high)//2
            tmp = query(1, mid, 1, 1, n)

            if tmp < a[-1]:
                low = mid+1
            else:
                high = mid -1
        update(low, 1, 1, n, -1)
        print(low)
