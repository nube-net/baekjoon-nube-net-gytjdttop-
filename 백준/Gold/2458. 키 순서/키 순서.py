import sys
inputF = sys.stdin.readline

n, m = map(int, inputF().split())
a = [set() for _ in range(n)]  # 큰 학생
b = [set() for _ in range(n)]  # 작은 학생

for _ in range(m):
    x, y = map(int, inputF().split())
    a[x-1].add(y-1)
    b[y-1].add(x-1)

for i in range(n):
    # 작은 학생
    Map_b = set()
    tmp_b = set()
    tmp_b.update(b[i])
    while tmp_b:
        q = tmp_b.pop()
        if q in Map_b:
            continue
        else:
            Map_b.add(q)
            b[i].add(q)
            tmp_b.update(b[q])

    # 큰 학생
    Map_a = set()
    tmp_a = set()
    tmp_a.update(a[i])
    while tmp_a:
        p = tmp_a.pop()
        if p in Map_a:
            continue
        else:
            Map_a.add(p)
            a[i].add(p)
            tmp_a.update(a[p])

count = 0
for i in range(n):
    if len(a[i]) + len(b[i]) == n-1:
        count +=1

print(count)
