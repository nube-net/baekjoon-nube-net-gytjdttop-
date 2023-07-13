import sys
from collections import deque
input = sys.stdin.readline

def round1(N) :
    if (N-int(N)) >= 0.5 :
        return int(N)+1
    else :
        return int(N)
n= int(input())
if n!=0:
    level = []
    for i in range(n) :
        level.append(int(input().rstrip()))
    
    level.sort()
    level=deque(level)
    num= round1(n*0.15)
    
    for k in range(num) :
        level.pop()
        level.popleft()
    
    result = sum(level)/len(level)
    print(round1(result))
else :
    print(0)