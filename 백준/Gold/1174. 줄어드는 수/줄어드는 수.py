from itertools import combinations
import sys

n = int(sys.stdin.readline())
s = {'0','1','2','3','4','5','6','7','8','9'}

cases = []
for i in range(1,11):
    for x in list(combinations(s, i)):
        x = list(x)
        x.sort(reverse=True)
        cases.append(int(''.join(x)))

cases.sort()
try:
    print(cases[n-1])
except:
    print(-1)
