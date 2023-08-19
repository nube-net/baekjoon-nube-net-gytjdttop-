import sys

inputF = sys.stdin.readline

n= int(inputF())
S = set()
for _ in range(n):
    x, y = map(int, inputF().split())
    tmp = y/x
    if tmp in S:
        continue
    else:
        S.add(tmp)
print(len(S))