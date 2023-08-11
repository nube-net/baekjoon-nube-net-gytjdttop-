import sys
inputF = sys.stdin.readline

num =[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
while True:
    if num[-1] >= 1000000000:
        break
    num.append(num[-1]+num[-2])

T = int(inputF())

for _ in range(T):
    n = int(inputF())
    tmp = []
    end= len(num)
    while True:
        for i in range(end):
            if num[i] > n:
                n -= num[i-1]
                tmp.append(num[i-1])
                break
        if n == 0:
            break
    print(*tmp[::-1])