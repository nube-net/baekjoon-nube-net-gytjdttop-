import  sys
input = sys.stdin.readline

n = int(input())
b = list(map(int, input().split()))
ans = []
a3 = set()
a2= []
for i in b:
    if i%3 == 0:
        a3.add(i)
    else:
        a2.append(i)
a2.sort()
cur = 0
tmp = []
if a2:
    cur = a2[0]
else:
    cur = a3.pop()
    tmp.append(cur)

while a3:
    if cur%2 == 0 and (cur//2 in a3):
        next = cur//2
        a3.remove(next)
        tmp.append(next)
        cur =next
    elif cur*3 in a3:
        next = cur*3
        a3.remove(next)
        tmp.append(next)
        cur = next
    else:
        ans.append(tmp)
        tmp = []
        cur = a3.pop()
        tmp.append(cur)
if tmp:
    ans.append(tmp)

for i in range(len(ans)):
    while ans[i]:
        print(ans[i].pop(), end=" ")
if a2:
    print(*a2)