import sys
inputF = sys.stdin.readline

T = int(inputF())

for _ in range(T):
    dic = {}

    n = int(inputF())
    for i in range(n):
        x, y = map(str, inputF().split())
        if y in dic:
            dic[y].append(x)
        else:
            dic[y] = [x]
    result = 1
    for k in dic:
        result *= len(dic[k])+ 1

    print(result-1)