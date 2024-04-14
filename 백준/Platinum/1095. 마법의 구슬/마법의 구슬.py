import sys
input =sys.stdin.readline

def cal(pn,num):
    tmp = num
    d = 0
    while tmp // pn > 0:
        tmp //= pn
        d += tmp
    return d

s, f, m = map(int, input().split())
prime = []
cnt = []
b = 1000000
dp = [True] * (b+1)
dp[0] = False
dp[1] = False
for k in range(2, int(b**0.5) + 1):
    if dp[k] == True:
        for i in range(k * k, b + 1, k):
            dp[i] = False
for i in range(b+1):
    if dp[i]:
        prime.append(i)
        cnt.append(cal(i,s+f)-cal(i,s)-cal(i,f))

ans = 1
for i in range(m, 0, -1):
    tmp = i
    flag = True
    for j in range(len(prime)):
        count = 0
        while tmp % prime[j] == 0:
            tmp //= prime[j]
            count += 1

        if count > cnt[j]:
            flag =False
            break
    if flag:
        ans = i
        break

print(ans)