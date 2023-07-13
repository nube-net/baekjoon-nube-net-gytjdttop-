import sys

n = int(sys.stdin.readline())

str0 = []
dic = {}
for i in range(n):
    a = sys.stdin.readline().rstrip()
    str0.append(a)
    for k in range(len(a)):
        if not (a[k] in dic) :
            dic[a[k]] = 0
        dic[a[k]] -= 10**(len(a)-k-1)
tmp = set(dic.items())
tmp = sorted(tmp, key = lambda x : x[1])

#
result=0
num=9
for o in tmp :
    result += num*(-1)*o[1]
    num-=1

print(result)
'''
print(dic)
print(tmp)
'''