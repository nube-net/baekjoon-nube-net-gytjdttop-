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

def update(idx, node, left, right):
    if idx < left or idx > right:
        return stree[node]
    if left == right:
        stree[node] =1
        return stree[node]

    mid = left + (right - left) // 2
    l_val = update(idx, 2 * node, left, mid)
    r_val = update(idx, 2 * node + 1, mid + 1, right)
    stree[node] = merge(l_val, r_val)
    return stree[node]

n = int(input())
arr = [0] * (n + 1) # 전후 체크
stree = [0] * (4 * (n + 1))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
S = {}  # 인덱스 저장
for i in range(n):
    S[B[i]] = i
build(stree, 1, 1, n)
ans = 0
for num in A:
    idx = S[num]+1
    update(idx, 1, 1, n)
    #print(query(idx+1, n, 1, 1, n))
   # print()
    ans += query(idx + 1, n, 1, 1, n)
print(ans)