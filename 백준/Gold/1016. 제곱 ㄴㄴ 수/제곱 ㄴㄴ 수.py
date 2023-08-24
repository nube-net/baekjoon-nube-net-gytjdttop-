import sys
input = sys.stdin.readline

a, b = map(int, input().split())
dp = [1]*(b-a+1)
result = b-a+1
cnt = 0
for i in range(2, int(b**0.5)+1):
    k = i**2
    for j in range((((a-1)//k)+1)*k, b+1, k):
        if dp[j-a] == 1:
            dp[j-a] = 0
            cnt += 1
print(result - cnt)

