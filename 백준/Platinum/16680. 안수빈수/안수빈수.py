import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    cur = str(n)+'0'*len(str(n))
    cur = int(cur)
    k=True
    while True:
        cnt = 0
        if cur >1e18:
            break
        for i in str(cur):
            cnt += int(i)
        if cnt%2:
            print(cur)
            k=False
            break
        else:
            cur += n
    if k:
        print(-1)
