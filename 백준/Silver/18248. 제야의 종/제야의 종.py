import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: sum(x))

for i in range(m):
    cur = a[0][0]
    for j in range(n):
        if cur == 1 and a[j][i]==0:
            print("NO")
            exit()
        cur = a[j][i]
print("YES")
        