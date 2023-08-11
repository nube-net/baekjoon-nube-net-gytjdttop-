import sys
inputF = sys.stdin.readline

n = int(inputF())
a = list(map(int, inputF().split()))
a.sort()

if n == 1:
    print(1)
else:
    x = sum(a[:-1])
    b = a[-1]

    if x+1 >= b:
        print(x+b)
    else:
        print(2*x + 1)


