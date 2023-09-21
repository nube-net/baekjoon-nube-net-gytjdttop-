import sys
input = sys.stdin.readline

# N^2 o
n, k = map(int, input().split())
dp = [0 for _ in range(n+1)]
for i in range(n+1):  # 초기 설정
    dp[i] = 1

for _ in range(1,k):  # 현재 계산에 사용된 숫자 개수-1
    tmp = [0 for _ in range(n + 1)]
    tmp[0] = 1
    for i in range(1,n+1):
        tmp[i] = (tmp[i-1] + dp[i])%1000000000
    dp = list(tmp)
    # print(sum(dp))

print(dp[n]%1000000000)