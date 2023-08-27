import sys
inputF = sys.stdin.readline

k, n = map(int, inputF().split())  # 보유, 필요
L = [int(inputF()) for _ in range(k)]

st = 1
end = max(L)    

while st <= end:  
    tmp = 0
    dx = (st + end ) // 2
    for i in L:
        tmp += i // dx

    if tmp < n:
        end = dx - 1
    else:
        st = dx + 1


print(end)
