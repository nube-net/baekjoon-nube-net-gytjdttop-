import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(k)]  # 사자
b = [int(input()) for _ in range(n-k)]
tmp = 0
for i in range(1, k):
    tmp += abs(a[i] - a[i - 1])
if n == k:
    print(tmp)
    exit()

M1, m1, M2, m2 = max(a), min(a), max(b), min(b)
if M1 < M2:
    tmp += min((M2-M1)*2, abs(a[0]-M2), abs(a[-1]-M2))
if m1 > m2:
    tmp += min((m1-m2)*2, abs(a[0]-m2), abs(a[-1]-m2))
print(tmp)


