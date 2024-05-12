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

n, m= map(int, input().split())
arr = [0 for _ in range(n+1)]
stree = [0] * (4 * (n + 1))

build(stree, 1, 1, n)
for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 1:
        update(a, b, 1, 1, n)
    else:
        if a > b:
            a,b =b,a
        print(query(a, b, 1, 1, n))

