import sys
input = sys.stdin.readline

def merge(left, right):
    return left + right

def build(stree, arr, node, left, right):
    if left == right:
        stree[node] = arr[left]
        return stree[node]
    mid = (left + right) // 2
    l_val = build(stree, arr, 2 * node, left, mid)
    r_val = build(stree, arr, 2 * node + 1, mid + 1, right)
    stree[node] = merge(l_val, r_val)
    return stree[node]

def update_lazy(stree, lazy, node, left, right):
    if lazy[node] != 0:
        stree[node] = (right - left + 1) - stree[node]
        if left != right:
            lazy[2 * node] ^= 1
            lazy[2 * node + 1] ^= 1
        lazy[node] = 0

def update(stree, lazy, start, end, node, left, right):
    update_lazy(stree, lazy, node, left, right)

    if end < left or start > right:
        return

    if start <= left and right <= end:
        lazy[node] ^= 1
        update_lazy(stree, lazy, node, left, right)
        return

    mid = (left + right) // 2
    update(stree, lazy, start, end, 2 * node, left, mid)
    update(stree, lazy, start, end, 2 * node + 1, mid + 1, right)
    stree[node] = merge(stree[2 * node], stree[2 * node + 1])

def query(stree, lazy, start, end, node, left, right):
    update_lazy(stree, lazy, node, left, right)

    if end < left or start > right:
        return 0

    if start <= left and right <= end:
        return stree[node]

    mid = (left + right) // 2
    l_val = query(stree, lazy, start, end, 2 * node, left, mid)
    r_val = query(stree, lazy, start, end, 2 * node + 1, mid + 1, right)
    return merge(l_val, r_val)

n, m = map(int, input().split())
arr = [0] * (n + 1)  
stree = [0] * (4 * (n + 1))
lazy = [0] * (4 * (n + 1))

build(stree, arr, 1, 1, n)

for _ in range(m):
    O, S, T = map(int, input().split())
    if O == 0:
        update(stree, lazy, S, T, 1, 1, n)
    else:
        print(query(stree, lazy, S, T, 1, 1, n))
