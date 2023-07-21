import sys
inputF = sys.stdin.readline

dp = [1,1,1]
for i in range(3,100):
    dp.append(dp[i-2]+dp[i-3])

T = int(inputF())

for _ in range(T):  # 테스트 케이스 수만큼
    print(dp[int(inputF())-1])