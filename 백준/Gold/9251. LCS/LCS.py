import sys
inputF = sys.stdin.readline

s1 = inputF().rstrip()
s2 = inputF().rstrip()

dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j - 1])

print(dp[len(s1)][len(s2)])

'''
처음 제출한 틀린 코드 n^2에 슬라이싱 시간이 더해져서 시간초과 떴음.
import sys
inputF = sys.stdin.readline

s1 = inputF().rstrip()
s2 = inputF().rstrip()

dp = [0] * len(s1)
dp0 = [0] * len(s1)
for i in range(len(s2)):
    for j in range(len(s1)):
        if s2[i] == s1[j]:
            if j == 0 :
                dp[j] = 1
            else:
                dp[j] = max(dp0[:j]) + 1
    dp0 = list(dp)
print(max(dp))
'''
