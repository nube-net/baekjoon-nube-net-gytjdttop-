import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0 for _ in range(n+1)] for _ in range(k)]
for i in range(n+1):
    dp[0][i] = 1
for i in range(1,k): # 현재 계산에 사용된 숫자 개수-1
    for num in range(n+1):  # num에 해당되는 조합 개수
        for j in range(n+1):
            if num + j >n:
                break
            dp[i][num+j] += dp[i-1][num]

print(dp[k-1][n]%1000000000)