import sys
from collections import  deque

n, k = map(int, sys.stdin.readline().split())
line = list(map(int, sys.stdin.readline().split()))

result = 1000000
c = 0
key = True
a=deque()
tmp=deque()  # 더미
for i in range(n):
    if line[i] == 1:
        a.append(i)

if len(a) < k:
    print(-1)
else:
    st=0
    en= 0
    for _ in range(k):  # 첫번째 집합
        b = a.popleft()
        if _ == 0:
            st = b
        if _ == k-1:
            en = b
        tmp.append(b)
    result = min(result, en-st+1)
    tmp.popleft()
    while a:
        st = tmp.popleft()
        en = a.popleft()
        tmp.append(en)
        result = min(result, en - st + 1)

    print(result)