#집합 활용(파이썬통과), n^3플로이드와샬(pypy통과)
# 다른분 풀이보니 효율적인건 DFS, BFS였음

#집합 활용 풀이
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
'''
# 기본 플로이드-와샬 알고리즘 활용
import sys
inputF = sys.stdin.readline

n, bus = map(int, inputF().split())
count =0
order = [[float('inf')]*n for _ in range(n)]
for i in range(n):
    order[i][i] = 0

for _ in range(bus): 
    x, y= map(int, inputF().split())
    order[x-1][y-1] = 1

for i in range(n):
    for j in range(n):  
        for k in range(n):  
            order[j][k] = min(order[j][k], order[j][i] + order[i][k])
tmp = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if order[i][j] == float('inf'):
            order[i][j] = 0
        elif order[i][j] !=0:
            tmp[j] += 1
            tmp[i] += 1

print(tmp.count(n-1))
'''
