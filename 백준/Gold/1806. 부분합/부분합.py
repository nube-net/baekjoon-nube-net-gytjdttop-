import sys
input = sys.stdin.readline
n, S = map(int, input().split())
nums = list(map(int, input().split()))

st, end = 0, 0
sum_ = 0
length = 100000

while True:
    if sum_ >= S:
        length = min(length, end - st)
        sum_ -= nums[st]
        st += 1
    elif end == n:
        break
    else:
        sum_ += nums[end]
        end += 1

if length == 100000:
    print(0)
else:
    print(length)