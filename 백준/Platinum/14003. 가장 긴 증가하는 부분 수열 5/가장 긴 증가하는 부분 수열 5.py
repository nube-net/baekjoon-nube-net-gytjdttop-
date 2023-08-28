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
memorize = [[]for _ in range(len(A))]
memorize[0].append((A[0],0))  # 수, 인덱스
memo_idx = 0
cur_idx = 0
for i in range(1, len(A)):
    if LIS[cnt] < A[i]:
        cnt += 1
        LIS[cnt] = A[i]
        cur_idx = cnt
        memorize[memo_idx].append((A[i], cnt))
    else:
        idx = bs(0, cnt, A[i])
        LIS[idx] = A[i]
        if cur_idx >= idx:
            memo_idx += 1
        memorize[memo_idx].append((A[i], idx))
        cur_idx = idx

print(cnt+1)
# print(*LIS[:cnt+1])
ans = []
for i in range(len(A)-1, -1, -1):
    while memorize[i]:
        x, y = memorize[i].pop()
        if y == cnt:
            cnt -= 1
            ans.append(x)
print(*ans[::-1])

