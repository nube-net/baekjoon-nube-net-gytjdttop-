a, b = map(str, input().rstrip().split())
if len(a) < len(b):
    print(0)
else:
    if a == b:
        print(a.count('8'))
    else:
        cnt = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                if a[i] == '8':
                    cnt +=1
                continue
            else:
                break
        print(cnt)
