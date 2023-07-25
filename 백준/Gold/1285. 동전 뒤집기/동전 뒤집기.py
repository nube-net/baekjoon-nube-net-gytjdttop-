import sys

n = int(sys.stdin.readline())

coins = [[] for _ in range(n)]
for i in range(n):
    tmp0 = sys.stdin.readline().rstrip()
    for k in range(n):
        if tmp0[k] == 'H':
            coins[i].append(0)
        else:
            coins[i].append(1)

result = n*n
tmp=0
for bit in range(1<<n):
    for i in range(n):
        if (bit^tmp)&(1<<i): 
            for k in range(n):
                coins[k][i] = 1-coins[k][i] 

    tmp = bit 

    result_tmp = sum(min(sum(x), n - sum(x)) for x in coins)
    result = min(result, result_tmp)

print(result)
