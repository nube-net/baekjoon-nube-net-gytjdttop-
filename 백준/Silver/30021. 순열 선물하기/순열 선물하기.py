n = int(input())
if n == 1:
    print("YES")
    print(1)
elif n == 2:
    print("NO")
else:
    print("YES")
    print('1 3 2', end=' ')
    if n > 3:
        for i in range(4,n+1):
            print(i, end=' ')