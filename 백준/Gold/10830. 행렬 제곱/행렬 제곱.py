import sys
inputF = sys.stdin.readline

n, b = map(int, inputF().split())
a = [list(map(int, inputF().split())) for _ in range(n)]
c = 1000

result = [[0]*n for _ in range(n)]
for i in range(n):
    result[i][i] = 1

while b > 0:
    if b % 2 == 1:
        Q = [[0]*n for _ in range(n)]
        for j in range(n):
            for i in range(n):  
                for x, y in zip(result[j], [a[_][i] for _ in range(n)]):
                    Q[j][i] += x*y
                    Q[j][i] %= c
        result = list(Q)
    
    Q = [[0]*n for _ in range(n)]
    for j in range(n):
        for i in range(n):  
            for x, y in zip(a[j], [a[_][i] for _ in range(n)]):
                Q[j][i] += x*y
                Q[j][i] %= c
    a = list(Q)
    b = b // 2

for row in result:
    print(*row)
