import sys
input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([x - 1, y - 1, i])
ans = []
a.sort()
up = []
down = []
a2 = []
for i in range(n):
    if a[i][0] < i:
        down.append([a[i], i - a[i][0]])
    elif a[i][0] > i:
        up.append([a[i], a[i][0] - i])
    else:
        a2.append(a[i])

for cur, cnt in up:
    x, y, idx = cur
    for _ in range(cnt):
        ans.append([idx + 1, "U"])
        x -= 1
    a2.append([x, y, idx])

for cur, cnt in reversed(down):
    x, y, idx = cur
    for _ in range(cnt):
        ans.append([idx + 1, "D"])
        x += 1
    a2.append([x, y, idx])


a2.sort(key=lambda x: x[1])
visit = [False for _ in range(n)]
a3 = []  
for i in range(n):
    if not visit[a2[i][1]]:
        visit[a2[i][1]] = True
    else:
        a3.append(i)

not_fill = [i for i in range(n) if not visit[i]]

a3.sort(key=lambda i: a2[i][1])
for i in range(len(a3)):
    idx = a3[i]
    nxt = not_fill[i]
    if a2[idx][1] < nxt:
        for _ in range(nxt - a2[idx][1]):
            ans.append([a2[idx][2] + 1, "R"])
        a2[idx][1] = nxt
    else:
        for _ in range(a2[idx][1] - nxt):
            ans.append([a2[idx][2] + 1, "L"])
        a2[idx][1] = nxt

print(len(ans))
for i in ans:
    print(*i)
