a = input()
if len(a) == 1:
    a += '0'
n = a
cnt = 0


while True:
    cnt += 1
    tmp = int(a[0]) + int(a[1])
    tmp %= 10
    a = a[1] + str(tmp)
    if a == n:
        break
print(cnt)
