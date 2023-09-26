import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
b = list(input().rstrip())
S ={'R':0,'G':1,'B':2}
for i in range(n):
    b[i] = S[b[i]]
ans = float('inf')

for s in range(3):
    a = list(b)
    tmp = 0
    for i in range(n-2):
        if a[i] == s:
            continue
        else:
            cnt = 0
            while a[i] != s:
                cnt +=1
                a[i] =(a[i]+1)%3
            a[i+1] = (a[i+1] + cnt) % 3
            a[i + 2] = (a[i + 2] + cnt) % 3
            tmp+=cnt
    if a[-1] == s and a[-2]==s:
        ans = min(ans,tmp)
if ans == float('inf'):
    ans = -1
print(ans)