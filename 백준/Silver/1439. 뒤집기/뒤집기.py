import sys
from collections import deque
a = sys.stdin.readline().rstrip()
a= deque(a)

key =2
zero = 0
one = 0
for i in a:
    if i == '0':
        if key != 0:
            key = 0
            zero += 1
    elif i == '1':
        if key != 1:
            key = 1
            one += 1

print(min(zero, one))
