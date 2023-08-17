import sys
inputF = sys.stdin.readline

n = int(inputF())
p = [list(map(int, inputF().split())) for _ in range(n)]
p.sort(key=lambda x: sum(x))
result = sum(p[-1]) - sum(p[0])
p.sort(key=lambda x: x[0]-x[1])

result = max(result, (p[-1][0]-p[-1][1]) - (p[0][0]-p[0][1]))
print(result)
