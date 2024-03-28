import sys
input =sys.stdin.readline

n, m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
prefix,min_, max_ = [0]*(n+1), [0] * (n+1), [0] * (n+1)

for i in range(n):  # 누적합 배열
    prefix[i+1] = prefix[i]+arr[i]

min_[1], max_[n] = prefix[1], prefix[n]
for i in range(2, n+1):  # i이전 최소값 저장
    min_[i] = min(min_[i-1], prefix[i])
for i in range(n-1, 0, -1):  # i이후 최대값 저장
    max_[i] = max(max_[i + 1], prefix[i])

ans = [0]*(n+1)
for i in range(m,n+1):  # i까지 최대 기댓값
    ans[i] = max_[i] - min_[i-m]

print(max(ans))