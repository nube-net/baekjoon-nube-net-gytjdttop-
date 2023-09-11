import math
import sys
input = sys.stdin.readline

def code(n):  #약수 구하기 코드
    nums = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n%i == 0):
            nums.append(i)
            if ((i**2) != n):
                nums.append(n // i)
    nums.sort()
    return nums

n = int(input())
S = [int(input()) for _ in range(n)]
S.sort()
tmp = [S[i+1]-S[i] for i in range(n-1)]
ans = math.gcd(*tmp)
print(*code(ans)[1:])