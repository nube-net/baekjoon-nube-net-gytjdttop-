import sys
input = sys.stdin.readline

n = int(input())
a = [[] for _ in range(n)]
iq = list(map(int, input().split()))
# 각 정점의 형제와 자식들을 일렬로 펼치면된다.
for _ in range(n - 1):
    x, y = map(int, input().split())
    a[x - 1].append((iq[y - 1], y - 1))  # (IQ, 번호)

for i in range(n):
    if a[i]:
        a[i].sort(reverse=True)  # IQ 높은 순 정렬
        for j in range(1, len(a[i])):
            print(a[i][j - 1][1] + 1,a[i][j][1] + 1)
        print(i + 1,a[i][0][1] + 1)
