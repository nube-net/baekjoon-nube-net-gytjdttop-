import math
import itertools
import sys
input = sys.stdin.readline
def code(n,a):  #약수 구하기 코드
    nums = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            if (i%a == 0):
                nums.append(i)
            if ((i ** 2) != n):
                if ((n // i) % a == 0):
                    nums.append(n // i)
    nums.sort()
    return nums
a, b = map(int, input().split())
if a == b:
    print(a,b)
    exit()
ans = code(b, a)
A = float('inf')
B = []
for x, y in list(itertools.combinations(ans,2)):
    if math.lcm(x,y) == b:
        if x + y < A:
            B = [x,y]
            A = x+y
print(*sorted(B))