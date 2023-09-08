import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = list(map(int, input().split()))
S = set(S[1:])
ans = set()
tmp = []

for _ in range(m):
    a = list(map(int, input().split()))
    tmp.append(a)

while True:
    L = len(S)
    for i in range(m):
        if i in ans:
            continue
        b = tmp[i]
        if any(j in S for j in b[1:]):
            S.update(b[1:])
            ans.add(i)
    if len(S) == L:  
        break

print(m-len(ans))
