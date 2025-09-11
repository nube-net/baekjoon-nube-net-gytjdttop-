import sys
input = sys.stdin.readline

a =list(map(int,input().split()))
m = sum(a)
M = a[0]*4+a[1]*6+a[2]*8+a[3]*12+a[4]*20
ans = []
while m <= M:
    ans.append(m)
    ans.append(M)
    m+=1
    M-=1
    if m == M:
        ans.append(m)
        break
print(*ans[::-1])
    