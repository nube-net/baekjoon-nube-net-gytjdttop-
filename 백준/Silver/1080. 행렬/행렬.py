import sys

n, m = map(int, sys.stdin.readline().split())

a = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]


count = 0
if n < 3 or m < 3:
    if a != b:
        print(-1)
    else: 
        print(0)
else:
    for i in range(n-2):  # 세로 이동
        for k in range(m-2):  # 가로 이동
            if a[i][k] == b[i][k]:
                continue
            else:
                count +=1
                for x in range(i,i+3):
                    for y in range(k,k+3):
                        if a[x][y] ==0:
                            a[x][y] = 1
                        else:
                            a[x][y] = 0
    if a == b:
        print(count)
    else:
        print(-1)