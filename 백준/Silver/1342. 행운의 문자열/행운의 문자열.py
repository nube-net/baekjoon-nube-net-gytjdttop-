import sys
import math
input = sys.stdin.readline

a = list(input().rstrip())
stack = []
n = len(a)
ans = 0
S = set()
def code(s,S):
    global ans
    if len(s) == n:
        ans +=1
    else:
        for i in range(n):
            if i in S:
                continue
            if s:
                if a[s[-1]] == a[i]:
                    continue
            s.append(i)
            S.add(i)
            code(s,S)
            s.pop()
            S.remove(i)
code(stack,S)
for i in set(a):
    x = a.count(i)
    ans //= math.factorial(x)
print(ans)

