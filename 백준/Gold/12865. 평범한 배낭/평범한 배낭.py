import sys
inputF = sys.stdin.readline

n, k = map(int, inputF().split())

dp = [0]*(k+1)

for _ in range(n):
    x, y = map(int, inputF().split())  # 무게, 가치

    for i in range(k, 0, -1):  # 역순 탐색
        if x > i:
            break
        else:
            dp[i] = max(dp[i], dp[i-x] + y)

print(max(dp))
