import sys
from collections import deque
input = sys.stdin.readline

Big = {2:1, 4:4, 5:5, 3:7, 6:9, 7:8}
Small = {2:'1', 3:'7', 4:'4', 5:'2', 6:'0', 7:'8'}  # 중간 숫자면 6 = 0
dp = ['0']*101

for i in Small:
    dp[i] = Small[i]
dp[8] = '10'
dp[6] = '6'

for i in range(9,101):
    dp[i] = '99'+ dp[i-1]
    for j in Small:
        dp[i] = str(min(int(dp[i-j] + Small[j]), int(dp[i])))

T = int(input())
for _ in range(T):
    n= int(input())
    print(dp[n], end=' ')
    if n%2 == 0:
        print('1'*(n//2))
    else:
        print('7'+ '1' * (n // 2-1))

