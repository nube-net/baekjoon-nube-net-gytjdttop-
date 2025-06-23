import sys
input = sys.stdin.readline
t = int(input())
for __ in range(t):
    n = int(input())
    N = int(n)
    cur =2
    ans = 1
    while n>1:
        tmp = 1
        x=1
        while n%cur == 0:
          tmp+=cur**x
          n /= cur
          x+=1
        cur += 1
        if tmp >1:
            ans *= tmp
    if N == ans-N:
        print(f"{str(N)} is a perfect number.")
        print()
    elif N > ans-N:
        print(f"{str(N)} is a deficient number.")
        print()
    else:
        print(f"{str(N)} is an abundant number.")
        print()
    