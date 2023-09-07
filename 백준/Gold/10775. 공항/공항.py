import sys
inputF = sys.stdin.readline


def find(a):
    path = []
    while S[a] != a:
        path.append(a)
        a = S[a]
    for node in path:
        S[node] = a
    return a

g = int(inputF())
p = int(inputF())
S = [i for i in range(g + 1)]
order = [int(inputF()) for _ in range(p)]  # 입력 값 - 도킹 가능한 게이트
ans = 0
for i in order:
    tmp = find(i)
    if S[tmp] != 0:
        ans += 1
        S[tmp] -= 1
    else: break

print(ans)