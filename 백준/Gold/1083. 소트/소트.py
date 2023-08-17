import sys
inputF = sys.stdin.readline

n = int(inputF())
nums = list(map(int, inputF().split()))
s = int(inputF())

tmp = []
while nums:
    if s <= 0:
        break
    k = s
    if s >= n:
        a = max(nums)
        s -= nums.index(a)
        tmp.append(a)
        nums.remove(a)
    else:
        a = max(nums[:s+1])
        s -= nums.index(a)
        tmp.append(a)
        nums.remove(a)

tmp += nums

print(*tmp)