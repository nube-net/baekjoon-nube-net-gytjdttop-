from heapq import heappop,heappush,heapify
import sys
input = sys.stdin.readline

def power(a,b):
    tmp = 1
    while b > 0:
        if b % 2 == 1:
            tmp = (tmp * a)
        a = (a * a)
        b = b // 2
    return tmp
b = 2000003
dp = [True] * (b+1)
dp[0] = False
dp[1] = False
for k in range(2, 2000004):
    if dp[k] == True:
        for i in range(k * k, b + 1, k):
            dp[i] = False
pq, ans_pq = [], []
heapify(pq)
heapify(ans_pq)
n = int(input())

for i in range(1, 22):
    d = 2**(i - 1)
    for j in range(b+1):
        if dp[j]:
            tmp = power(j,d)
            if tmp > 2000003:
                break
            heappush( pq, (tmp,i,j))
cur = 0
ans = 1
check = [0]*(b+1)
for _ in range(n):
    val, cnt, id = heappop(pq)
    heappush(ans_pq, (-val, cnt,id))

while ans_pq:
    tmp,_,id = heappop(ans_pq)
    ans *= -tmp
    ans%= 2000003
print(ans)


