import sys

n = int(sys.stdin.readline())
dp_max = [0, 0, 0]
dp_min = [0, 0, 0]
tmp = []

for i in range(n):
    num = list(map(int, sys.stdin.readline().split()))

    dp_max = [num[0] + max(dp_max[:2]), num[1] + max(dp_max), num[2] + max(dp_max[1:])]
    dp_min = [num[0] + min(dp_min[:2]), num[1] + min(dp_min), num[2] + min(dp_min[1:])]

print(max(dp_max), min(dp_min))