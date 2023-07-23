a, b, c = map(int, input().split())
tmp = 1
while b > 0:
    if b % 2 == 1:
        tmp = (tmp * a) % c
    a = (a * a) % c
    b = b // 2
print(tmp)
