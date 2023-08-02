import sys
inputF = sys.stdin.readline

n = int(inputF())

dp = [1] * (n + 1)
num = [0]
num1 = list(map(int, inputF().split()))
num += num1

for i in range(1, n+1):
    for k in range(1, i):
        if num[k] < num[i]:
            dp[i] = max(dp[i], dp[k]+1)

result = max(dp)
print(result)