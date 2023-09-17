import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline
# map(int, input().split())
# map(str, input().strip().split())
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
a,b =map(int, input().split())

if b>= a:
    print('NO')
else:
    ans = []
    while a != b:
        if a >= 2 and b>= 1:
            a -= 2
            b -= 1
            ans.append('aba')
        else:
            break
        if a ==0 or b== 0:
            break
    if a!=b:
        print('NO')
    else:
        for _ in range(a):
            ans[0]+= 'ba'
        print('YES')
        print(len(ans))
        for i in ans:
            print(i)