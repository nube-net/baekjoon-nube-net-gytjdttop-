import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]
arr.sort(key = lambda x: (x[1]))
a = [0]*2001
ans = 0
tmp = 0
for st, end, box in arr:
    tmp = box

    for i in range(st, end):
        if c < a[i] + tmp: # 초과 용량
            tmp = c-a[i]
    for i in range(st, end):
        a[i] += tmp
    ans += tmp

print(ans)

