import sys
input = sys.stdin.readline

n = int(input())
S = set()
cnt = 0
for _ in range(n):
    a,b = map(int, input().split())
    if b:
        if a in S:
            cnt += 1
        else:
            S.add(a)
    else:
        if a in S:
            S.remove(a)
        else:
            cnt += 1

print(cnt + len(S))