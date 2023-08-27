import sys
inputF = sys.stdin.readline

n, m = map(int, inputF().split())
data = [list(map(int, inputF().split())) for _ in range(n)]
ans = [0, -1]  # 무게 가격
pre = -1
data.sort(key=lambda x: (x[1], -x[0]))
result = float('inf')
for i in range(n):
    x, y = data[i]
    ans[0] += x
    if pre == y:
        ans[1] += y
    else:
        ans[1] = y
    pre = y
    if ans[0] >= m:
        result = min(result, ans[1])
if result ==  float('inf'):
    print(-1)
else:
    print(result)