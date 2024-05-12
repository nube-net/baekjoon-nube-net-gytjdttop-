import sys
import math

def merge(left, right):
    return (left * right) % 1000000007

def build(arr, stree, node, left, right):
    if left == right:
        stree[node] = arr[left]
        return stree[node]

    mid = (left + right) // 2
    l_val = build(arr, stree, 2 * node, left, mid)
    r_val = build(arr, stree, 2 * node + 1, mid + 1, right)
    stree[node] = merge(l_val, r_val)
    return stree[node]

def query(start, end, node, left, right):
    if end < left or start > right:
        return 1

    if start <= left and right <= end:
        return stree[node]

    mid = (left + right) // 2
    l_val = query(start, end, 2 * node, left, mid)
    r_val = query(start, end, 2 * node + 1, mid + 1, right)
    return merge(l_val, r_val)

def update(idx, val, node, left, right):
    if idx < left or idx > right:
        return

    if left == right:
        stree[node] = val
        return

    mid = (left + right) // 2
    update(idx, val, 2 * node, left, mid)
    update(idx, val, 2 * node + 1, mid + 1, right)
    stree[node] = merge(stree[2 * node], stree[2 * node + 1])

N, M, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
stree = [0] * (4 * N)

build(arr, stree, 1, 0, N-1)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1: 
        update(b-1, c, 1, 0, N-1)
    else: 
        print(query(b-1, c-1, 1, 0, N-1))
