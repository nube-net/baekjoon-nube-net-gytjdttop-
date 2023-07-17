import sys
from collections import deque
n = int(sys.stdin.readline())

sum0 = [[0] for _ in range(1000)]

Q = deque()
Q.append(1)
Q.append(2)
for i in range(2,1000):
    tmp = sum(Q)
    tmp%=10007
    Q.append(tmp)
    Q.popleft()
    sum0[i] = tmp

if n == 1:
    print(1)
elif n ==2:
    print(2)
else:
    print(sum0[n-1])