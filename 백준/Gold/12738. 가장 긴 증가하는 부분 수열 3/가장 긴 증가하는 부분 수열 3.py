import sys
input = sys.stdin.readline

def bs(st, end, a, LIS):
    while st < end:
        dx = (st + end) // 2
        if LIS[dx] >= a:
            end = dx
        else:
            st = dx +1
    return end

n = int(input())
A = list(map(int, input().split()))
LIS = [-float('inf')]

for i in A:
    if LIS[-1] < i:
        LIS.append(i)
    else:
        idx = bs(0, len(LIS) - 1, i, LIS)
        LIS[idx] = i

print(len(LIS) - 1)

