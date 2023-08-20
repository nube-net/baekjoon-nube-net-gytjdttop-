# 100점 코드
from math import gcd
import sys
inputF = sys.stdin.readline

n = int(inputF())
S = set()
for _ in range(n):
    x, y = map(int, input().split())
    
    g = gcd(y, x)
    tmp = (y//g, x//g)
    
    S.add(tmp)
    
print(len(S))
'''
# 이건 10점 짜리 코드
import sys

inputF = sys.stdin.readline

n= int(inputF())
S = set()
for _ in range(n):
    x, y = map(int, inputF().split())
    tmp = y/x
    if tmp in S:
        continue
    else:
        S.add(tmp)
print(len(S))
'''
