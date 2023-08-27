import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    visit = set()
    Q = deque()
    A, B = map(int, sys.stdin.readline().rstrip().split())
    Q.append((A, ''))

    while Q:
        n, s = Q.popleft()

        if n == B:
            print(s)
            break

        # D
        tmp = (n * 2) % 10000
        if tmp not in visit:
            visit.add(tmp)
            Q.append((tmp, s + 'D'))

        # S
        if n > 0:
            tmp = n - 1
        else:
            tmp = 9999
        if tmp not in visit:
            visit.add(tmp)
            Q.append((tmp, s + 'S'))

        # L
        tmp = (n % 1000) * 10 + (n // 1000)
        if tmp not in visit:
            visit.add(tmp)
            Q.append((tmp, s + 'L'))

        # R
        tmp = (n % 10) * 1000 + (n // 10)
        if tmp not in visit:
            visit.add(tmp)
            Q.append((tmp, s + 'R'))
