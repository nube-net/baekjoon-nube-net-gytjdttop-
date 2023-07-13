import sys

n = int(sys.stdin.readline().rstrip())
children = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n + 1)  #최장 수열 ㄹㅇ 개빡침
for child in children:
    dp[child] = dp[child - 1] + 1

answer = n - max(dp)
print(answer)