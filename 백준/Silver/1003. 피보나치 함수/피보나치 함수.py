import sys


T = int(sys.stdin.readline())

for i in range(T):
    Q = [[1, 0], [0, 1]]
    n = int(sys.stdin.readline())
    if n == 0 :
        print(f"{1} {0}")
    elif n == 1:
        print(f"{0} {1}")
    else:
        for k in range(n-1):
            tmp = Q[0]
            Q.remove(tmp)
            x = tmp[0] + Q[-1][0]
            y = tmp[1] + Q[-1][1]
            Q.append([x, y])
        print(*Q[-1])



