import sys
inputF = sys.stdin.readline

n = int(inputF())
a = set(map(int, inputF().split()))
m = int(inputF())
b = list(map(int, inputF().split()))
c = [0 for _ in range(m)]
for i in range(m):
    if b[i] in a:
        c[i] = 1

print(*c)
