import sys
input = sys.stdin.readline

n = int(input())
ans = []
tmp = []
for _ in range(n):
    val = list(input().rstrip())
    idx = []
    for i in range(len(val)-1,-1,-1):
        if val[i] == '6' or val[i] == '9':
            idx.append(i)
            val[i] = '6'
    tmp.append([val,idx])

for i in range(1,n):
    cur = int("".join(tmp[i][0]))
    pre = int("".join(tmp[i-1][0]))
    #print(cur)
    if cur >= pre:
        ans.append(cur)
        #print(cur,i)
        continue
    k = True
    for j in tmp[i][1]:
        tmp[i][0][j] = '9'
        cur = int("".join(tmp[i][0]))
        if cur >= pre:
            for p in range(j+1,len(tmp[i][0])):
                if tmp[i][0][p] == '9':
                    tmp[i][0][p] = '6'
                    if pre <= int("".join(tmp[i][0])):
                        continue
                    else:
                        tmp[i][0][p] = '9'
            cur = int("".join(tmp[i][0]))
            ans.append(cur)
            #print(cur,i)
            k = False
            break

    if k:
        print("impossible")
        exit()
print("possible")
print("".join(tmp[0][0]))
for i in range(len(ans)):
    print(ans[i])




