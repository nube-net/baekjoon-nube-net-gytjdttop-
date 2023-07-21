import sys
inputF = sys.stdin.readline

n, m = map(int, inputF().split())
dic= {}

for _ in range(n):
    x, y = map(str, inputF().split())
    dic[x] = y

for i in range(m):
    tmp = inputF().rstrip()
    sys.stdout.write(dic[tmp]+'\n')