import sys
input = sys.stdin.readline

n, m = map(int, input().split())
DNA = [input().rstrip() for _ in range(n)]

ans = []
cnt = 0
for i in range(m):
    dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(n):
        dic[DNA[j][i]] += 1

    s = ''
    c = -1
    for _ in dic:
        if dic[_] > c:
            s = _
            c = dic[_]
    ans.append(s)
    cnt += n-c
print(''.join(ans))
print(cnt)