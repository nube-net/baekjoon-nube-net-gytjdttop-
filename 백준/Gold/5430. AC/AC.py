import sys
from re import sub
from collections import deque
inputF = sys.stdin.readline

T = int(inputF())

for _ in range(T):
    num = []
    order = inputF().rstrip()  # 원본
    n = int(inputF())
    tmp = inputF().rstrip()
    a=''
    for k in range(len(tmp)):
        if tmp[k].isdigit() :
            a += tmp[k]
        else:
            if a == '':
                continue
            else:
                num.append(int(a))
                a = ''

    num = deque(num)
    key = False
    t= 0  # 현재 순방향
    for x in range(len(order)):  # 명령어 읽기
        if order[x] == 'R':
            t = 1 - t
        elif order[x] == 'D':
            if num:
                if t:
                    num.pop()
                else:
                    num.popleft()
            else:
                key = True
                break
    if key:
        print("error")
    else:
        if t:
            num.reverse()
        result = str(list(num))
        print(result.replace(' ', ''))