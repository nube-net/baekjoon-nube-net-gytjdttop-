import sys
inputF = sys.stdin.readline

n = int(inputF())

dp = [1] * (n + 1)
children = [0]
for _ in range(n):
    children.append(int(inputF()))

for i in range(1, n+1):
    for k in range(1, i):
        if children[k] < children[i]:
            dp[i] = max(dp[i], dp[k]+1)

result = n - max(dp)
print(result)