import sys
input = sys.stdin.readline


for __ in range(3):
    n = int(input())
    size = 0
    coins = []
    for _ in range(n):
        coin, m = map(int, input().split())
        coins.append([coin,m])
        size += coin*m
    if size%2 == 1:
        print(0)
        continue

    dp = [True if _ == 0 else False for _ in range(size//2 +1)]
    l= len(dp)
    for coin, m in coins:
        
        for i in range(l-1,coin-1,-1):
            if dp[i - coin]:
                for j in range(m):
                    if coin*j + i > l-1:
                        break
                    dp[ coin*j + i]=True
        if dp[-1]:
            break

    if dp[-1]:
        print(1)
    else:
        print(0)