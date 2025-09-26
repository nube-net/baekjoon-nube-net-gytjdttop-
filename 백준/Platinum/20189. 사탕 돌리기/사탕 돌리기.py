import sys
input = sys.stdin.readline

n,k,q = map(int,input().split())
can = [{} for _ in range(n)]  # candy boxes
cnt = 0
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in tmp:
        if j-1 < i:
            cnt +=1
        if j-1 == i:
            continue
        elif j-1 in can[i]:
            can[i][j-1] +=1
        else:
            can[i][j-1] = 1
#print(can)
#print(cnt)
if not can[0]:
    cnt+=1
if cnt > q:
    print(0)
else:
    print(1)