import sys
import math
from collections import deque
from itertools import combinations
input = sys.stdin.readline
# map(int, input().split())
# map(str, input().strip().split())
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
dic = {}
a, b= map(int, input().split())
if a > b:
    print(2*b + 1)
elif a == b:
    print(2 * (b-1) + 1)
else:
    if a == 1 or a == 0:
        print(0)
    else:
        print(2*a -1)

