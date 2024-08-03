n = str(input())
l = len(n)
ans = 0
tmp = [ int(s) for s in n]

k = True
cur = list(tmp)
if True:
    tmp = list(cur)
    val = 1
    check = False
    for s in tmp:
        if s != 0:
            check = True
        if check:
            val *= s
    ans = max(ans, val)
for i in range(l):
    tmp = list(cur)

    if tmp[i] != 0:
        tmp[i] -= 1
    val = 1
    check = False
    for j in range(l):
        if j > i:
            val *= 9
            continue
        if tmp[j] != 0:
            check = True
        if check:
            val *= tmp[j]
    ans = max(ans, val)


print(ans)
