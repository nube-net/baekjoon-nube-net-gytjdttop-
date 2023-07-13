import sys
inputF = sys.stdin.readline

n = int(inputF())
stack = [0]  # 스택
result = []

num = []  # 숫자 사용 여부
for o in range(n):
    num.append(o+1)

tmp=0
for i in range(n) :
    a = int(inputF())
    if stack[-1] != a and not(a in num) :
        result = ["NO"]
        break
    elif stack[-1] != a:
        for k in range(a-tmp):
            if num:
                stack.append(num[0])
                result.append("+")
                num.remove(num[0])
            else :
                result = ["NO"]
                break
        if result == ["NO"]:
            break
        if stack[-1] == a:
            result.append("-")
            tmp = max(tmp, stack.pop())
        else:
            result = ["NO"]
            break
    else:
        result.append("-")
        stack.pop()


for x in result:
    print(x)