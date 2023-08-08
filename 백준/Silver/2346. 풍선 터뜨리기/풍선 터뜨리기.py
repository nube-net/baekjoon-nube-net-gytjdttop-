import sys
from collections import deque
inputF = sys.stdin.readline

n = int(inputF())
a = list(map(int, inputF().split()))
balloons = deque()  # 큐
for i in range(n):
    balloons.append((a[i],i+1))  # 종이, 풍선번호

result = []
num = 1
while balloons:
    if num > 0:
        for _ in range(num-1):
            tmp = balloons.popleft()
            balloons.append(tmp)
        
        x, y  = balloons.popleft()
        num = x
        result.append(y)
    
    else:
        for _ in range(abs(num)):
            tmp = balloons.pop()
            balloons.appendleft(tmp)

        x, y  = balloons.popleft()
        num = x
        result.append(y)
print(*result)