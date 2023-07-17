import sys
inputF = sys.stdin.readline

n = int(inputF())

a = list(map(int, inputF().split()))  # 리스트 원본
b = set(a)  # 집합
b = sorted(b)

tmp = 0
dic = {}
for i in b:
    if not (i in dic):
        dic[i] = tmp
        tmp += 1

for k in a:
    print(dic[k], end=" ")


