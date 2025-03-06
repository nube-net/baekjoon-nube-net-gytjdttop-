import sys
input = sys.stdin.readline

def cal(d):
    cur = 0
    tmp = 0

    for i in range(1, n):
        cur += d
        tmp += abs(cur - idx[i])

    return tmp

n = int(input())
idx = list(map(int, input().split()))

left, right = 1, 1000000001

while right - left > 2:
    mid_l = left + (right - left)//3
    mid_r = right - (right - left)//3

    L = cal(mid_l)
    R = cal(mid_r)

    if L <= R:
        right = mid_r
    else:
        left = mid_l

print(min(cal(left), cal(left + 1), cal(right)))
