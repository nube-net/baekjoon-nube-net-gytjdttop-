import sys
input = sys.stdin.readline
# 세그 트리
def merge(left, right):
    return min(left, right)

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
        return float('inf')  # 최솟값 얻기 위해 무한대 값을 반환

    if start <= left and right <= end:
        return stree[node]

    mid = left + (right - left) // 2
    l_val = query(start, end, 2 * node, left, mid)
    r_val = query(start, end, 2 * node + 1, mid + 1, right)
    return merge(l_val, r_val)

def update(idx, val, node, left, right):
    if idx < left or idx > right:
        return stree[node]
    if left == right:
        stree[node] = val
        return stree[node]

    mid = left + (right - left) // 2
    l_val = update(idx, val, 2 * node, left, mid)
    r_val = update(idx, val, 2 * node + 1, mid + 1, right)
    stree[node] = merge(l_val, r_val)
    return stree[node]

n, m = map(int, input().split())
arr = [0] * (n + 1)
stree = [0] * (4 * (n + 1))

for i in range(1, n + 1):
    arr[i] = int(input())

build(stree, 1, 1, n)

for _ in range(m):
    a, b = map(int, input().split())
    print(query(a, b, 1, 1, n))
