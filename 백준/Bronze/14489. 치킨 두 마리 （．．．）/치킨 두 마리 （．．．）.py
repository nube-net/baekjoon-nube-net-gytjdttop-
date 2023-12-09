a,b = map(int, input().split())
n = int(input())

if a+b >= n+n:
    print(a+b-n-n)
else:
    print(a+b)