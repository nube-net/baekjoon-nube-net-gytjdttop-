import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dv(s, e, l, r):
    global ans
    if s > e:
        return
    #print(s,e)
    m = (s + e) // 2
    k = max(l, m - d)
    #print(k)
    
    #######
    for i in range(k, r + 1):
        if (m-k) * temp[m] + val[k] < (m - i) * temp[m] + val[i]:
            k = i
    ########
    ans = max(ans, (m-k) * temp[m] + val[k])
    dv(s, m - 1, l, k)
    dv(m + 1, e, k, r)


n, d = map(int, input().split())
temp = [0] + list(map(int, input().split()))
val = [0] + list(map(int, input().split()))
ans = float('-inf')

dv(1, n, 1, n)

print(ans)
