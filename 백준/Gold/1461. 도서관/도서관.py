import sys
from collections import deque
inputF = sys.stdin.readline

n, m = map(int, inputF().split())
num = list(map(int, inputF().split()))
num.sort()  # 시간 복잡도 최대 n 제곱
num = deque(num)

neg= []
for _ in range(n):
    tmp = num.popleft()
    if tmp <0:
        neg.append(tmp)
    else:
        num.appendleft(tmp)
        break
result =0

if neg:
    for i in range(0,len(neg),m):
        result -= 2*neg[i]


if num:
    for o in range(len(num)-1,-1 ,-m):
        result += 2*num[o]

if num and neg:
    if num[-1]>= -neg[0]:
        result -= num[-1]
    else:
        result += neg[0]
elif num:
    result -= num[-1]
else:
    result += neg[0]
print(result)
