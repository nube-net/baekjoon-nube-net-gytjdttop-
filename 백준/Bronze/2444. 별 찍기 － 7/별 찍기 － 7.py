import sys
inputF = sys.stdin.readline

n = int(inputF())

for i in range(n):
    tmp = '*'*(2*i + 1)
    print(tmp.center(2*n, ' ').rstrip())
for i in range(n-2,-1,-1):
    tmp = '*'*(2*i + 1)
    print(tmp.center(2*n, ' ').rstrip())