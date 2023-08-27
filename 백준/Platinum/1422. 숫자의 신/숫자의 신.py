import sys
input = sys.stdin.readline

k, n = map(int, input().split())
S = [input().rstrip() for _ in range(k)]
S.sort(key=lambda x: x*12)

index = k-1
a = 1
for i in range(k-1,-1,-1):
    if len(S[i]) > a:
        index = i
        a = len(S[i])

ans= ''
for i in range(k-1,-1,-1):
    ans += S[i]
    if i == index:
        for _ in range(n-k):
            ans += S[i]
print(ans)