import sys
inputF = sys.stdin.readline
n = int(inputF())
num = [i**2 for i in range(1, int(n**(1/2)) + 1)]  # n 이하 제곱수
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    if i in num:
        dp[i] = 1
    else:
        dp[i] = min([dp[i - j] + 1 for j in num if i - j > 0])
print(dp[n])
