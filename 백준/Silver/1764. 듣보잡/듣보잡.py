import sys
inputF = sys.stdin.readline

n, m = map(int, inputF().split())
a=set()
b=set()

for i in range(n):
    a.add(inputF().rstrip())
for k in range(m):
    b.add(inputF().rstrip())

result = []
for p in a:
    if p in b:
        result.append(p)
result.sort()
print(len(result))
for _ in result:
    print(_)