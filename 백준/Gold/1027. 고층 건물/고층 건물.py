from math import gcd
import sys
input = sys.stdin.readline

# 우측 목표 사이에 더 큰 기울기 있으면 안됨
n = int(input())
h = list(map(int, input().split()))
result = [0]*n

for i in range(n-1):
    tmp = -1000000001
    for j in range(i+1, n):
        x, y = j-i, h[j] - h[i]
        g = gcd(y, x)
        x, y = x//g, y//g
        if tmp < y/x:
            tmp = y/x
            result[i] += 1
            result[j] += 1
print(max(result))