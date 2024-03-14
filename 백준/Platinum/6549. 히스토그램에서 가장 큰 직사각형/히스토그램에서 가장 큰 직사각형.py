import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def find(a):
    if S[a] != a:
        S[a] = find(S[a])
    return S[a]

def union(a, b): # (a를 b 쪽으로)
    root_a = find(a)
    root_b = find(b)
    S[root_a] = root_b

while True:
    a = list(enumerate(map(int, input().split())))
    n = a[0][1]
    if n == 0:
        break
    a = a[1:]
    # print(a)
    S = [i for i in range(n)]  # 분리집합 index
    check = [False]*n  # 방문 여부
    length = [0]*n  # 연속된 직사각형 넓이
    ans = 0
    a.sort(key=lambda x: -x[1])
    for idx,cur in a:
        idx -= 1
        check[idx] = True
        if idx < n-1 and check[idx+1]:
            id = find(idx+1)
            length[idx] += length[id]
            length[id] = 0
            union(idx+1,idx)
        if idx > 0 and check[idx-1]:
            id = find(idx-1)
            length[idx] += length[id]
            length[id] = 0
            union(idx-1,idx)
        length[idx] += 1
        ans = max(ans, length[idx]*cur)
    print(ans)

