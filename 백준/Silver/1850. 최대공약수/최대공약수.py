import sys
import math
n, m = map(int, sys.stdin.readline().split())

print('1'*math.gcd(n,m))