import sys
input = sys.stdin.readline
def find(a):
    if S[a] != a:
        S[a] = find(S[a])
    return S[a]

def union(a, b):
    root_a = find(a)
    root_b = find(b)

    S[root_a] = root_b
    if root_a != root_b:
        cnt[root_b] += cnt[root_a]


T = int(input())
for _ in range(T):
    n = int(input())
    S = {}
    cnt = {}

    for __ in range(n):
        a, b = map(str,input().split())
        if a not in S:
            S[a] = a
            cnt[a] = 1

        if b not in S:
            S[b] = b
            cnt[b] = 1

        union(a,b)
        print(cnt[find(a)])
