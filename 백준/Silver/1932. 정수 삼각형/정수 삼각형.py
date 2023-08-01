import sys
inputF = sys.stdin.readline

n = int(inputF())
a = [list(map(int, inputF().split() ))for _ in range(n)]
dp = [ [0]*(_+1) for _ in range(n)]


for i in range(n):  # 층수
    if i == 0:
        dp[i][i] = a[i][i]
    else:

        for k in range(i):  # 칸수

            dp[i][k] = max(dp[i][k], a[i][k] + dp[i-1][k])

            dp[i][k+1] = max(dp[i][k+1], a[i][k+1] + dp[i-1][k])

print(max(dp[n-1]))