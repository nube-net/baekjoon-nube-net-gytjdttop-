import sys
n = int(sys.stdin.readline())
a = 1
for i in range(n-1):
    if i%2 == 0:
        a = a*2 +1
    else:
        a = a*2 -1
    a %= 10007
print(a)




