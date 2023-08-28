import sys
input = sys.stdin.readline

def bs(st, end, a):
    while st < end:
        dx = (st + end) // 2
        if LIS[dx] >= a:
            end = dx
        else:
            st = dx +1
    return end

n = int(input())
A = list(map(int, input().split()))
LIS = [-float('inf')] * len(A)
cnt = 0
LIS[0] = A[0]
for i in range(1, len(A)):
    if LIS[cnt] < A[i]:
        cnt += 1
        LIS[cnt] = A[i]
    else:
        idx = bs(0, cnt, A[i])
        LIS[idx] = A[i]

print(cnt+1)

